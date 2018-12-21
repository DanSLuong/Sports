from flask import (Flask,
                    render_template,
                    request, redirect,
                    jsonify,
                    url_for,
                    flash,
                    g)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player, Game, TeamStats, League, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from functools import wraps

app = Flask(__name__)

APPLICATION_NAME = "Sports App"
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

# Connect to the Database and creates a session
engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print("access token received %s " % access_token)

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    '''
        Due to the formatting for the result from the server token exchange we
        have to split the token first on commas and select the first index
        which gives us the key : value for the server access token then we split
        it on colons to pull out the actual token value and replace the
        remaining quotes with nothing so that it can be used directly in the
        graph api calls
    '''
    token = result.split(',')[0].split(':')[1].replace('"', '')

    url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?access_token=%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px;' \
              'height: 300px;' \
              'border-radius: 150px;' \
              '-webkit-border-radius: 150px;' \
              '-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px;' \
              'height: 300px;' \
              'border-radius: 150px;' \
              '-webkit-border-radius: 150px;' \
              '-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print("done!")
    return output


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showTeams'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showTeams'))


# Require Login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('showLogin', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# Homepage
@app.route('/')
def home():
    games = session.query(Game).all()
    return render_template('scores.html', games=games)


# Scores
@app.route('/scores/')
def scores():
    games = session.query(Game).all()
    """
    for game in games:
        teamstats = session.query(TeamStats).filter_by(game_id=game.id).all()
    """
    # return render_template('scores.html', games=games, teamstats=teamstats)
    return render_template('scores.html', games=games)


# Game Data/Box Score Stats
# @app.route('/<int:game_id>/')
@app.route('/boxscore/<int:game_id>/')
def boxScore(game_id):
    games = session.query(Game).filter_by(id=game_id).one()
    teams = session.query(Team).filter_by(id=games.team_id).all()
    players = session.query(Player).filter_by(team_id=teams.id).all()
    teamstats = session.query(TeamStats).filter_by(game_id=game_id).all()
    return render_template('boxscore.html',
                            games=games,
                            teams=teams,
                            players=players,
                            teamstats=teamstats)


# List the different Leagues
@app.route('/leagues/')
def leagues():
    leagues = session.query(League).all()
    return render_template('leagues.html', leagues=leagues)


# Create new League
@app.route('/leagues/new/', methods=['GET', 'POST'])
@login_required
def createLeague():
    if request.method == 'POST':
        newLeague = League(name=request.form['name'],
                            sport=request.form['sport'],
                            description=request.form['description'])
        session.add(newLeague)
        session.commit()
        return redirect(url_for('leagueInfo', league_id=newLeague.id))
    else:
        return render_template('newleague.html')


# Shows information about the selected sports league
@app.route('/leagues/<int:league_id>/')
@app.route('/leagues/<int:league_id>/teams/')
def leagueInfo(league_id):
    league = session.query(League).filter_by(id=league_id).one()
    teams = session.query(Team).filter_by(league_id=league_id).all()
    return render_template('leagueinfo.html', league=league, teams=teams)


# Add new team to the league
@app.route('/leagues/<int:league_id>/addteam/', methods=['GET', 'POST'])
@login_required
def addTeam(league_id):
    league = session.query(League).filter_by(id=league_id).one()
    if request.method == 'POST':
        newTeam = Team(name=request.form['name'])
        session.add(newTeam)
        session.commit()
        return redirect(url_for('leagueInfo', league_id=league_id))
    else:
        return render_template('newteam.html', league=league)


# Info page for each individual team that list the rosters and recent game scores
@app.route('/leagues/<int:league_id>/teams/<int:team_id>/')
def teamInfo(league_id, team_id):
    league = session.query(League).filter_by(id=league_id).one()
    team = session.query(Team).filter_by(id=team_id).one()
    # stats = session.query(TeamStats).filter_by(team_id=team_id).all()
    players = session.query(Player).filter_by(team_id=team_id).all()
    return render_template('roster.html', league=league, team=team, players=players)


# List all teams
@app.route('/teams/')
def teams():
    teams = session.query(Team).all()
    return render_template('teams.html', teams=teams)


# Add a new player to the selected team
@app.route('/leagues/<int:league_id>/teams/<int:team_id>/addplayer/', methods=['GET', 'POST'])
@login_required
def addPlayer(league_id, team_id):
    if login_session['user_id'] != team.user_id:
        return "<script>function myFunction() " \
               "{alert('You can only add players to teams you have created.');}" \
               "</script><body onload='myFunction()'>"
    team = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        newPlayer = Player(firstName=request.form['firstName'],
                            lastName=request.form['lastName'],
                            team_id=team_id)
        session.add(newPlayer)
        session.commit()
        return redirect(url_for('teamInfo', league_id=league_id, team_id=team_id))
    else:
        return render_template('newplayer.html', team=team)


# List of all players
@app.route('/players/')
def players():
    players = session.query(Player).all()
    return render_template('players.html', players=players)


# Shows infromation about the selected player
@app.route('/leagues/<int:league_id>/teams/<int:team_id>/players/<int:player_id>/')
def playerStats(league_id, team_id, player_id):
    players = session.query(Player).filter_by(id=player_id)
    team = session.query(Team).filter_by(id=team_id).one()
    return render_template('player.html', players=players, team=team)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
