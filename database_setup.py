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
    league = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return{
            'name': self.name,
            'league': self.league,
            'id': self.id,
        }


# Player table to store player info
class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    
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
            'id': self.id,
        }


# Game table to sort games and dates.
class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    date = Column(String(250), nullable=False)

    # Each game associates with two teams
    hometeam_id = Column(Integer, ForeignKey('team.id'))
    hometeam = relationship(Team, backref=backref('game', cascade='all, delete'))
    awayteam_id = Column(Integer, ForeignKey('team.id'))
    awayteam = relationship(Team, backref=backref('game', cascade='all, delete'))

    hometeam_id = Column(Integer, ForeignKey('teamstats.id'))
    hometeam = relationship(Team, backref=backref('game', cascade='all, delete'))
    awayteam_id = Column(Integer, ForeignKey('teamstats.id'))
    awayteam = relationship(Team, backref=backref('game', cascade='all, delete'))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
            # 'date': self.date,
            'date': self.date,
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