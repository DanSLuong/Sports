from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Team, Player, PlayerStats, Game, User

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Default NBA Teams
team1 = Team(name = 'Hawks', city = 'Atlanta', state = 'Georgia', conference = 'East', division = 'Southeast', league = 'NBA')
session.add(team1)
team2 = Team(name = 'Celtics', city = 'Boston', state = 'Massachusetts', conference = 'East', division = 'Atlantic', league = 'NBA')
session.add(team2)
team3 = Team(name = 'Nets', city = 'Brooklyn', state = 'New York', conference = 'East', division = 'Atlantic', league = 'NBA')
session.add(team3)
team4 = Team(name = 'Hornets', city = 'Charlotte', state = 'North Carolina', conference = 'East', division = 'Southeast', league = 'NBA')
session.add(team4)
team5 = Team(name = 'Bulls', city = 'Chicago', state = 'Illinois', conference = 'East', division = 'Central', league = 'NBA')
session.add(team5)
team6 = Team(name = 'Cavaliers', city = 'Cleveland', state = 'Ohio', conference = 'East', division = 'Central', league = 'NBA')
session.add(team6)
team7 = Team(name = 'Mavericks', city = 'Dallas', state = 'Texas', conference = 'West', division = 'Southwest', league = 'NBA')
session.add(team7)
team8 = Team(name = 'Nuggets', city = 'Denver', state = 'Colorado', conference = 'East', division = 'Northwest', league = 'NBA')
session.add(team8)
team9 = Team(name = 'Pistons', city = 'Detroit', state = 'Michigan', conference = 'East', division = 'Central', league = 'NBA')
session.add(team9)
team10 = Team(name = 'Warriors', city = 'Golden State', state = 'California', conference = 'West', division = 'Pacific', league = 'NBA')
session.add(team10)
team11 = Team(name = 'Rockets', city = 'Houston', state = 'Texas', conference = 'West', division = 'Southwest', league = 'NBA')
session.add(team11)
team12 = Team(name = 'Pacers', city = 'Indiana', state = 'Indiana', conference = 'East', division = 'Central', league = 'NBA')
session.add(team12)
team13 = Team(name = 'Clippers', city = 'Los Angeles', state = 'California', conference = 'West', division = 'Pacific', league = 'NBA')
session.add(team13)
team14 = Team(name = 'Lakers', city = 'Los Angeles', state = 'California', conference = 'West', division = 'Pacific', league = 'NBA')
session.add(team14)
team15 = Team(name = 'Grizzlies', city = 'Memphis', state = 'Tennessee', conference = 'West', division = 'Southwest', league = 'NBA')
session.add(team15)
team16 = Team(name = 'Heat', city = 'Miami', state = 'Florida', conference = 'East', division = 'Southeast', league = 'NBA')
session.add(team16)
team17 = Team(name = 'Bucks', city = 'Milwaukee', state = 'Wisconsin', conference = 'East', division = 'Central', league = 'NBA')
session.add(team17)
team18 = Team(name = 'Timberwolves', city = 'Minnesota', state = 'Minnesota', conference = 'West', division = 'Northwest', league = 'NBA')
session.add(team18)
team19 = Team(name = 'Pelicans', city = 'New Orleans', state = 'Louisiana', conference = 'West', division = 'Southwest', league = 'NBA')
session.add(team19)
team20 = Team(name = 'Knicks', city = 'New York', state = 'New York', conference = 'East', division = 'Atlantic', league = 'NBA')
session.add(team20)
team21 = Team(name = 'Thunder', city = 'Oklahoma City', state = 'Oklahoma', conference = 'West', division = 'Northwest', league = 'NBA')
session.add(team21)
team22 = Team(name = 'Magic', city = 'Orlando', state = 'Florida', conference = 'East', division = 'Southeast', league = 'NBA')
session.add(team22)
team23 = Team(name = '76ers', city = 'Philadelphia', state = 'Pennsylvania', conference = 'East', division = 'Atlantic', league = 'NBA')
session.add(team23)
team24 = Team(name = 'Suns', city = 'Phoenix', state = 'Arizona', conference = 'West', division = 'Pacific', league = 'NBA')
session.add(team24)
team25 = Team(name = 'Trail Blazers', city = 'Portland', state = 'Oregon', conference = 'West', division = 'Northwest', league = 'NBA')
session.add(team25)
team26 = Team(name = 'Kings', city = 'Sacramento', state = 'California', conference = 'West', division = 'Pacific', league = 'NBA')
session.add(team26)
team27 = Team(name = 'Spurs', city = 'San Antonio', state = 'Texas', conference = 'West', division = 'Southwest', league = 'NBA')
session.add(team27)
team28 = Team(name = 'Raptors', city = 'Toronto', state = 'Canada', conference = 'East', division = 'Atlantic', league = 'NBA')
session.add(team28)
team29 = Team(name = 'Jazz', city = 'Utah', state = 'Utah', conference = 'West', division = 'Northwest', league = 'NBA')
session.add(team29)
team30 = Team(name = 'Wizards', city = 'Washington', state = 'Washington, D.C.', conference = 'East', division = 'Southeast', league = 'NBA')
session.add(team30)
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







"""
game1=Game(date = "November 15, 2018")
session.add(game1)





playerstats1=PlayerStats(game_id=1,
                        team_id=1,
                        minutesPlayed = 32,
                        points = 27,
                        rebounds = 3,
                        assists = 3,
                        steals = 2,
                        blocks = 0,
                        turnovers = 1,
                        fouls = 4)
session.add(playerstats1)


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

"""

