from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Team, Player, PlayerStats, Game, User

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



team1=Team(name='Rockets',
            city='Houston',
            state='Texas',
            conference='West',
            division='Southwest',
            league='NBA')
session.add(team1)


player1=Player(firstName="Carmelo",
                lastName="Anthony",
                jersey="7",
                position="F",
                height="6'8",
                weight="240",
                age="34",
                college="Syracuse",
                birthplace="NYC",
                role="Bench",
                team=team1)
session.add(player1)
session.commit()

player1=Player(firstName="James",
                lastName="Harden",
                jersey="13",
                position="G",
                height="6'5",
                weight="220",
                age="29",
                college="Arizona State",
                birthplace="Compton, California",
                role="Starter",
                team=team1)
session.add(player1)
session.commit()

player1=Player(firstName="Chris",
                lastName="Paul",
                jersey="3",
                position="G",
                height="6'0",
                weight="175",
                age="33",
                college="Wake Forest",
                birthplace="Winston-Salem, NC",
                role="Starter",
                team=team1)
session.add(player1)
session.commit()

player1=Player(firstName="Clint",
                lastName="Capela",
                jersey="15",
                position="C",
                height="6'10",
                weight="240",
                age="24",
                college="Elan Chalon",
                birthplace="Geneva, Switzerland",
                role="Starter",
                team=team1)
session.add(player1)
session.commit()

player1=Player(firstName="P.J.",
                lastName="Tucker",
                jersey="17",
                position="F",
                height="6'6",
                weight="245",
                age="33",
                college="Texas",
                birthplace="Raleigh, NC",
                role="Starter",
                team=team1)
session.add(player1)
session.commit()


player1=Player(firstName="James",
                lastName="Ennis III",
                jersey="8",
                position="F",
                height="6'7",
                weight="210",
                age="28",
                college="Long Beach State",
                birthplace="Ventura, California",
                role="Starter",
                team=team1)
session.add(player1)
session.commit()

player1=Player(firstName="Isaiah",
                lastName="Hartenstein",
                jersey="55",
                position="C",
                height="7'0",
                weight="249",
                age="20",
                college="",
                birthplace="",
                role="Bench",
                team=team1)
session.add(player1)
session.commit()

player1=Player(firstName="Gary",
                lastName="Clark",
                jersey="6",
                position="F",
                height="6'8",
                weight="225",
                age="23",
                college="",
                birthplace="",
                role="Bench",
                team=team1)
session.add(player1)
session.commit()

player1=Player(firstName="Eric",
                lastName="Gordon",
                jersey="10",
                position="G",
                height="6'4",
                weight="215",
                age="29",
                college="Indiana",
                birthplace="",
                role="Bench",
                team=team1)
session.add(player1)
session.commit()