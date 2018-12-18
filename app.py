from flask import (Flask,
                    render_template,
                    request, redirect,
                    jsonify,
                    url_for,
                    flash,
                    g)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player, TeamStats, Game, User
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
    for game in games:
        teamstats = session.query(TeamStats).filter_by(game_id=game.id).all()
    return render_template('scores.html', games=games, teamstats=teamstats)


# Game Data/Box Score Stats
# @app.route('/<int:game_id>/')
@app.route('/boxscore/<int:game_id>')
def boxScore(game_id):
    games = session.query(Game).filter_by(id=game_id).one()
    teams = session.query(Team).filter_by(id=games.team_id).all()
    players = session.query(Player).filter_by(team_id=teams.id).all()
    teamstats = session.query(TeamStats).filter_by(game_id=game_id).all()
    return render_template('boxscore.html',
                            games=games,teams=teams, players=players, teamstats=teamstats)


# Shows infromation about the selected player
@app.route('/<int:team_id>/players/<int:player_id>/')
def playerStats(team_id, player_id):
    players = session.query(Player).filter_by(id=player_id)
    team = session.query(Team).filter_by(id=team_id).one()
    return render_template('player.html', players=players, team=team)


@app.route('/addteam/', methods=['GET', 'POST'])
def addTeam():
    if request.method == 'POST':
        team = Team(name = request.form['name'],
                       league = request.form['league'])
        session.add(team)
        session.commit()
        return redirect(url_for('scores'))
    else:
        return render_template('newteam.html')

@app.route('/<int:team_id>/')
def team(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    stats = session.query(TeamStats).filter_by(team_id=team_id).all()
    players = session.query(Player).filter_by(team_id=team_id).all()
    return render_template('roster.html', team=team, stats=stats, players=players)


@app.route('/<int:team_id>/addplayer/', methods=['GET', 'POST'])
def addPlayer(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        newPlayer = Player(firstName=request.form['firstName'],
                            lastName=request.form['lastName'],
                            team_id=team_id)
        session.add(newPlayer)
        session.commit()
        return redirect(url_for('team', team_id=team_id))
    else:
        return render_template('newplayer.html', team=team)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)