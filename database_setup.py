import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


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


class PlayerStats(Base):
    __talbename__ 'playerstats'

    date = Column(date, nullable=False)
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


    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
            'date': self.date,
            'minutesPlayed': self.minutesPlayed,
            'points': self.points,
            'rebounds': self.rebounds,
            'assists': self.assists,
            'steals': self.steals,
            'blocks': self.blocks,
            'turnovers': self.turnovers,
            'fouls': self.fouls,
        }


engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)