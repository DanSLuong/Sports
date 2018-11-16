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
                birthplace="Raleigh, North Carolina",
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
                college="Zalgiris Kaunas",
                birthplace="Eugene, Oregon",
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
                college="Cincinnati",
                birthplace="Smithfield, North Carolina",
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
                birthplace="Indianapolis, Indiana",
                role="Bench",
                team=team1)
session.add(player1)
session.commit()







game1=Game(date = "November 13, 2018")
session.add(game1)
session.commit()




playerstats1=PlayerStats(game_id=1,
                        team_id=1,
                        minutesPlayed = 36,
                        points = 22,
                        rebounds = 5,
                        assists = 11,
                        steals = 3,
                        blocks = 1,
                        turnovers = 4,
                        fouls = 3)
session.add(playerstats1)
session.commit()

playerstats1=PlayerStats(game_id=1,
                        player_id=2,
                        team_id=1,
                        minutesPlayed = 32,
                        points = 21,
                        rebounds = 5,
                        assists = 4,
                        steals = 2,
                        blocks = 0,
                        turnovers = 3,
                        fouls = 0)
session.add(playerstats1)
session.commit()

playerstats1=PlayerStats(game_id=1,
                        player_id=3,
                        team_id=1,
                        minutesPlayed = 36,
                        points = 24,
                        rebounds = 9,
                        assists = 2,
                        steals = 0,
                        blocks = 1,
                        turnovers = 1,
                        fouls = 4)
session.add(playerstats1)
session.commit()

playerstats1=PlayerStats(game_id=1,
                        player_id=4,
                        team_id=1,
                        minutesPlayed = 40,
                        points = 12,
                        rebounds = 6,
                        assists = 2,
                        steals = 1,
                        blocks = 1,
                        turnovers = 1,
                        fouls = 3)
session.add(playerstats1)
session.commit()

playerstats1=PlayerStats(game_id=1,
                        player_id=5,
                        team_id=1,
                        minutesPlayed = 33,
                        points = 16,
                        rebounds = 4,
                        assists = 1,
                        steals = 1,
                        blocks = 2,
                        turnovers = 1,
                        fouls = 3)
session.add(playerstats1)
session.commit()

playerstats1=PlayerStats(game_id=1,
                        player_id=6,
                        team_id=1,
                        minutesPlayed = 11,
                        points = 3,
                        rebounds = 1,
                        assists = 0,
                        steals = 0,
                        blocks = 0,
                        turnovers = 2,
                        fouls = 3)
session.add(playerstats1)
session.commit()

playerstats1=PlayerStats(game_id=1,
                        player_id=7,
                        team_id=1,
                        minutesPlayed = 15,
                        points = 0,
                        rebounds = 2,
                        assists = 1,
                        steals = 0,
                        blocks = 0,
                        turnovers = 0,
                        fouls = 3)
session.add(playerstats1)
session.commit()

playerstats1=PlayerStats(game_id=1,
                        player_id=8,
                        team_id=1,
                        minutesPlayed = 33,
                        points = 11,
                        rebounds = 0,
                        assists = 2,
                        steals = 0,
                        blocks = 1,
                        turnovers = 2,
                        fouls = 1)
session.add(playerstats1)
session.commit()
