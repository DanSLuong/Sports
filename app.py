from flask import (Flask,
                    render_template,
                    request, redirect,
                    jsonify,
                    url_for,
                    flash,
                    g)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player, PlayerStats, Game, User
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
    return render_template('scores.html')


# Game Data/Box Score Stats
# @app.route('/<int:game_id>/')
@app.route('/boxscore')
def boxScore():
    return render_template('boxscore.html')


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
                       city = request.form['city'],
                       state = request.form['state'],
                       conference = request.form['conference'],
                       division = request.form['division'],
                       league = request.form['league'])
        session.add(team)
        session.commit()
        return redirect(url_for('scores'))
    else:
        return render_template('newteam.html')

@app.route('/<int:team_id>/')
def team(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(Player).filter_by(team_id=team_id).all()
    return render_template('roster.html', team=team, players=players)


@app.route('/<int:team_id>/addplayer/', methods=['GET', 'POST'])
def addPlayer(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        newPlayer = Player(firstName=request.form['firstName'],
                            lastName=request.form['lastName'],
                            jersey=request.form['jersey'],
                            position=request.form['position'],
                            height=request.form['height'],
                            weight=request.form['weight'],
                            age=request.form['age'],
                            college=request.form['college'],
                            birthplace=request.form['birthplace'],
                            role=request.form['role'],
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