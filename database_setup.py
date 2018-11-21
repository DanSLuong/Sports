import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# Team table to store the team info
class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(250), nullable=False)
    conference = Column(String(250), nullable=False)
    division = Column(String(250), nullable=False)
    league = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return{
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'conference': self.conference,
            'division': self.division,
            'league': self.league,
            'id': self.id,
        }


# Player table to store player info
class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    jersey = Column(Integer, nullable=False) 
    position = Column(String(250))
    height = Column(String(250))
    weight = Column(String(250))
    age = Column(Integer, nullable=False)
    college = Column(String(250))
    birthplace = Column(String(250))
    role = Column(String(250))
    
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team, backref=backref('player', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='items')


    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
            'firstName': self.firstName,
            'lastName': self.lastName,
            'jersey': self.jersey,
            'position': self.position,
            'height': self.height,
            'weight': self.weight,
            'age': self.age,
            'college': self.college,
            'birthplace': self.birthplace,
            'role': self.role,
            'id': self.id,
        }


# Game table to sort games and dates.
class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    date = Column(String(250), nullable=False)

    # Each game associates with two teams
    team1_id = Column(Integer, ForeignKey('team.id'))
    team1 = relationship(Team, backref=backref('game', cascade='all, delete'))
    team2_id = Column(Integer, ForeignKey('team.id'))
    team2 = relationship(Team, backref=backref('game', cascade='all, delete'))

    teamstats1_id = Column(Integer, ForeignKey('teamstats.id'))
    teamstats1 = relationship(Team, backref=backref('game', cascade='all, delete'))
    teamstats2_id = Column(Integer, ForeignKey('teamstats.id'))
    teamstats2 = relationship(Team, backref=backref('game', cascade='all, delete'))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
            # 'date': self.date,
            'date': self.date,
            'id': self.id,
        }


# Stats table for player stats from each individual game
class PlayerStats(Base):
    __tablename__ = 'playerstats'

    id = Column(Integer, primary_key=True)
    minutesPlayed = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    rebounds = Column(Integer, nullable=False)
    assists = Column(Integer, nullable=False)
    steals = Column(Integer, nullable=False)
    blocks = Column(Integer, nullable=False)
    turnovers = Column(Integer, nullable=False)
    fouls = Column(Integer, nullable=False)

    player_id = Column(Integer, ForeignKey('player.id'))
    player = relationship(Player, backref=backref('playerstats', cascade='all, delete'))
    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game, backref=backref('playerstats', cascade='all, delete'))


    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
            # 'date': self.date,
            'minutesPlayed': self.minutesPlayed,
            'points': self.points,
            'rebounds': self.rebounds,
            'assists': self.assists,
            'steals': self.steals,
            'blocks': self.blocks,
            'turnovers': self.turnovers,
            'fouls': self.fouls,
            'id': self.id,
        }


# Stats table for team stats from each individual game
class TeamStats(Base):
    __tablename__ = 'teamstats'

    id = Column(Integer, primary_key=True)
    q1 = Column(Integer)
    q2 = Column(Integer)
    q3 = Column(Integer)
    q4 = Column(Integer)
    finalscore = q1+q2+q3+q4

    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team, backref=backref('teamstats', cascade='all, delete'))
    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game, backref=backref('teamstats', casecade='all, delete'))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
            # 'date': self.date,
            'q1': self.q1,
            'q2': self.q2,
            'q3': self.q3,
            'q4': self.q4,
            'finalscore': self.finalscore,
            'id': self.id,
        }



engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)