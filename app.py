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

# Connect to the Database and creates a session
engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



# Homepage
@app.route('/')
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
@app.route('/boxscore/<int:game_id>')
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
@app.route('/leagues')
def leagues():
    leagues = session.query(League).all()
    return render_template('leagues.html', leagues=leagues)


# Create new League
@app.route('/leagues/new', methods=['GET', 'POST'])
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
@app.route('/leagues/<int:league_id>')
def leagueInfo(league_id):
    league = session.query(League).filter_by(id=league_id).one()
    teams = session.query(Team).filter_by(league_id=league_id).all()
    return render_template('leagueinfo.html', league=league, teams=teams)


# Add new team to the league
@app.route('/leagues/<int:league_id>/addteam/', methods=['GET', 'POST'])
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
    team = session.query(Team).filter_by(id=team_id).one()
    stats = session.query(TeamStats).filter_by(team_id=team_id).all()
    players = session.query(Player).filter_by(team_id=team_id).all()
    return render_template('roster.html', team=team, stats=stats, players=players)

# Add a new player to the selected team
@app.route('/leagues/<int:league_id>/teams/<int:team_id>/addplayer/', methods=['GET', 'POST'])
def addPlayer(league_id, team_id):
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
