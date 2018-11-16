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
                team=team11)
session.add(player1)

player2=Player(firstName="Chris",
                lastName="Paul",
                jersey="3",
                position="G",
                height="6'0",
                weight="175",
                age="33",
                college="Wake Forest",
                birthplace="Winston-Salem, NC",
                role="Starter",
                team=team11)
session.add(player2)

player3=Player(firstName="Clint",
                lastName="Capela",
                jersey="15",
                position="C",
                height="6'10",
                weight="240",
                age="24",
                college="Elan Chalon",
                birthplace="Geneva, Switzerland",
                role="Starter",
                team=team11)
session.add(player3)

player4=Player(firstName="P.J.",
                lastName="Tucker",
                jersey="17",
                position="F",
                height="6'6",
                weight="245",
                age="33",
                college="Texas",
                birthplace="Raleigh, North Carolina",
                role="Starter",
                team=team11)
session.add(player4)


player5=Player(firstName="James",
                lastName="Ennis III",
                jersey="8",
                position="F",
                height="6'7",
                weight="210",
                age="28",
                college="Long Beach State",
                birthplace="Ventura, California",
                role="Starter",
                team=team11)
session.add(player5)

player6=Player(firstName="Eric",
                lastName="Gordon",
                jersey="10",
                position="G",
                height="6'4",
                weight="215",
                age="29",
                college="Indiana",
                birthplace="Indianapolis, Indiana",
                role="Bench",
                team=team11)
session.add(player6)

player7=Player(firstName="Gary",
                lastName="Clark",
                jersey="6",
                position="F",
                height="6'8",
                weight="225",
                age="23",
                college="Cincinnati",
                birthplace="Smithfield, North Carolina",
                role="Bench",
                team=team11)
session.add(player7)

player8=Player(firstName="Isaiah",
                lastName="Hartenstein",
                jersey="55",
                position="C",
                height="7'0",
                weight="249",
                age="20",
                college="Zalgiris Kaunas",
                birthplace="Eugene, Oregon",
                role="Bench",
                team=team11)
session.add(player8)

player9=Player(firstName="Marquese",
                lastName="Chriss",
                jersey="0",
                position="F",
                height="6'10",
                weight="240",
                age="21",
                college="Washington",
                birthplace="Sacramento, California",
                role="Bench",
                team=team11)
session.add(player9)

player10=Player(firstName="Michael",
                lastName="Carter-Williams",
                jersey="1",
                position="G",
                height="6'6",
                weight="190",
                age="27",
                college="Syracuse",
                birthplace="Hamilton, Massachusetts",
                role="Bench",
                team=team11)
session.add(player10)

player11=Player(firstName="Vincent",
                lastName="Edwards",
                jersey="12",
                position="F",
                height="6'8",
                weight="225",
                age="22",
                college="Purdue",
                birthplace="Middletown, Ohio",
                role="Bench",
                team=team11)
session.add(player11)

player12=Player(firstName="Gerald",
                lastName="Green",
                jersey="14",
                position="G",
                height="6'7",
                weight="205",
                age="32",
                college="Gulf Shores Academy",
                birthplace="Houston, Texas",
                role="Bench",
                team=team11)
session.add(player12)





player13=Player(firstName="Kevin",
                lastName="Durant",
                jersey="35",
                position="F",
                height="6'9",
                weight="240",
                age="30",
                college="Texas",
                birthplace="Washington, D.C.",
                role="Starter",
                team=team10)
session.add(player13)

player14=Player(firstName="Draymond",
                lastName="Green",
                jersey="23",
                position="F",
                height="6'7",
                weight="230",
                age="28",
                college="Michigan State",
                birthplace="Saginaw, Michigan",
                role="Starter",
                team=team10)
session.add(player14)

player15=Player(firstName="Damian",
                lastName="Jones",
                jersey="15",
                position="C",
                height="7'0",
                weight="245",
                age="23",
                college="Vanderbilt",
                birthplace="Baton Rouge, Louisiana",
                role="Starter",
                team=team10)
session.add(player15)

player16=Player(firstName="Klay",
                lastName="Thompson",
                jersey="11",
                position="G",
                height="6'7",
                weight="215",
                age="28",
                college="Washington State",
                birthplace="Los Angeles, California",
                role="Starter",
                team=team10)
session.add(player16)

player17=Player(firstName="Andre",
                lastName="Iguodala",
                jersey="9",
                position="F",
                height="6'6",
                weight="215",
                age="34",
                college="Arizona",
                birthplace="Springfield, Illinois",
                role="Starter",
                team=team10)
session.add(player17)

player18=Player(firstName="Kevon",
                lastName="Looney",
                jersey="5",
                position="F",
                height="6'9",
                weight="220",
                age="22",
                college="UCLA",
                birthplace="Milwaukee, Wisconsin",
                role="Bench",
                team=team10)
session.add(player18)

player19=Player(firstName="Jonas",
                lastName="Jerebko",
                jersey="21",
                position="F",
                height="6'10",
                weight="231",
                age="31",
                college="Angelico Biella",
                birthplace="Kinna, Sweden",
                role="Bench",
                team=team10)
session.add(player19)

player20=Player(firstName="Shaun",
                lastName="Livingston",
                jersey="34",
                position="G",
                height="6'7",
                weight="192",
                age="33",
                college="Peoria Central HS",
                birthplace="Peoria, Illinois",
                role="Bench",
                team=team10)
session.add(player20)

player21=Player(firstName="Alfonzo",
                lastName="McKinnie",
                jersey="28",
                position="F",
                height="6'8",
                weight="215",
                age="26",
                college="Green Bay",
                birthplace="Chicago, Illinois",
                role="Bench",
                team=team10)
session.add(player21)

player22=Player(firstName="Quinn",
                lastName="Cook",
                jersey="4",
                position="G",
                height="6'2",
                weight="179",
                age="25",
                college="Duke",
                birthplace="Washington, D.C.",
                role="Bench",
                team=team10)
session.add(player22)

player23=Player(firstName="Jordan",
                lastName="Bell",
                jersey="28",
                position="F",
                height="6'9",
                weight="224",
                age="23",
                college="Oregon",
                birthplace="Los Angeles, California",
                role="Bench",
                team=team10)
session.add(player23)

player24=Player(firstName="Jacob",
                lastName="Evans",
                jersey="10",
                position="G",
                height="6'6",
                weight="210",
                age="21",
                college="Green Bay",
                birthplace="Jacksonville, North Carolina",
                role="Bench",
                team=team10)
session.add(player24)
session.commit()







playerstats1=PlayerStats(game_id = 1, player_id = 1, minutesPlayed = 32, points = 27, rebounds = 3, assists = 3, steals = 2, blocks = 0, turnovers = 1, fouls = 4)
session.add(playerstats1)
playerstats2=PlayerStats(game_id = 1, player_id = 2, minutesPlayed = 28, points = 10, rebounds = 5, assists = 7, steals = 3, blocks = 2, turnovers = 2, fouls = 1)
session.add(playerstats2)
playerstats3=PlayerStats(game_id = 1, player_id = 3, minutesPlayed = 29, points = 10, rebounds = 10, assists = 1, steals = 1, blocks = 0, turnovers = 0, fouls = 1)
session.add(playerstats3)
playerstats4=PlayerStats(game_id = 1, player_id = 4, minutesPlayed = 31, points = 3, rebounds = 4, assists = 1, steals = 0, blocks = 0, turnovers = 0, fouls = 3)
session.add(playerstats4)
playerstats5=PlayerStats(game_id = 1, player_id = 5, minutesPlayed = 32, points = 19, rebounds = 5, assists = 1, steals = 1, blocks = 0, turnovers = 0, fouls = 3)
session.add(playerstats5)
playerstats6=PlayerStats(game_id = 1, player_id = 6, minutesPlayed = 29, points = 17, rebounds = 0, assists = 3, steals = 1, blocks = 0, turnovers = 2, fouls = 3)
session.add(playerstats6)
playerstats7=PlayerStats(game_id = 1, player_id = 7, minutesPlayed = 27, points = 9, rebounds = 7, assists = 2, steals = 0, blocks = 2, turnovers = 0, fouls = 1)
session.add(playerstats7)
playerstats8=PlayerStats(game_id = 1, player_id = 8, minutesPlayed = 14, points = 6, rebounds = 5, assists = 1, steals = 0, blocks = 0, turnovers = 0, fouls = 1)
session.add(playerstats8)
playerstats9=PlayerStats(game_id = 1, player_id = 9, minutesPlayed = 3, points = 0, rebounds = 0, assists = 0, steals = 0, blocks = 0, turnovers = 0, fouls = 2)
session.add(playerstats9)
playerstats10=PlayerStats(game_id = 1, player_id = 10, minutesPlayed = 3, points = 1, rebounds = 1, assists = 1, steals = 0, blocks = 0, turnovers = 0, fouls = 1)
session.add(playerstats10)
playerstats11=PlayerStats(game_id = 1, player_id = 11, minutesPlayed = 3, points = 3, rebounds = 1, assists = 0, steals = 0, blocks = 0, turnovers = 0, fouls = 0)
session.add(playerstats11)
playerstats12=PlayerStats(game_id = 1, player_id = 12, minutesPlayed = 3, points = 2, rebounds = 0, assists = 0, steals = 0, blocks = 0, turnovers = 0, fouls = 1)
session.add(playerstats12)
session.commit()


playerstats13=PlayerStats(game_id = 1, player_id = 13, minutesPlayed = 29, points = 20, rebounds = 5, assists = 2, steals = 0, blocks = 1, turnovers = 2, fouls = 4)
session.add(playerstats13)
playerstats14=PlayerStats(game_id = 1, player_id = 14, minutesPlayed = 23, points = 0, rebounds = 5, assists = 5, steals = 1, blocks = 0, turnovers = 5, fouls = 1)
session.add(playerstats14)
playerstats15=PlayerStats(game_id = 1, player_id = 15, minutesPlayed = 18, points = 5, rebounds = 5, assists = 0, steals = 0, blocks = 1, turnovers = 1, fouls = 1)
session.add(playerstats15)
playerstats16=PlayerStats(game_id = 1, player_id = 16, minutesPlayed = 29, points = 10, rebounds = 3, assists = 0, steals = 0, blocks = 2, turnovers = 3, fouls = 3)
session.add(playerstats16)
playerstats17=PlayerStats(game_id = 1, player_id = 17, minutesPlayed = 23, points = 5, rebounds = 6, assists = 1, steals = 0, blocks = 0, turnovers = 1, fouls = 3)
session.add(playerstats17)
playerstats18=PlayerStats(game_id = 1, player_id = 18, minutesPlayed = 18, points = 12, rebounds = 5, assists = 1, steals = 0, blocks = 1, turnovers = 2, fouls = 3)
session.add(playerstats18)
playerstats19=PlayerStats(game_id = 1, player_id = 19, minutesPlayed = 20, points = 8, rebounds = 3, assists = 1, steals = 0, blocks = 0, turnovers = 0, fouls = 1)
session.add(playerstats19)
playerstats20=PlayerStats(game_id = 1, player_id = 20, minutesPlayed = 16, points = 2, rebounds = 2, assists = 3, steals = 1, blocks = 0, turnovers = 0, fouls = 1)
session.add(playerstats20)
playerstats21=PlayerStats(game_id = 1, player_id = 21, minutesPlayed = 12, points = 8, rebounds = 2, assists = 0, steals = 0, blocks = 0, turnovers = 1, fouls = 2)
session.add(playerstats21)
playerstats22=PlayerStats(game_id = 1, player_id = 22, minutesPlayed = 24, points = 11, rebounds = 2, assists = 1, steals = 0, blocks = 0, turnovers = 0, fouls = 1)
session.add(playerstats22)
playerstats23=PlayerStats(game_id = 1, player_id = 23, minutesPlayed = 12, points = 2, rebounds = 3, assists = 3, steals = 0, blocks = 0, turnovers = 0, fouls = 0)
session.add(playerstats23)
playerstats24=PlayerStats(game_id = 1, player_id = 24, minutesPlayed = 11, points = 3, rebounds = 3, assists = 1, steals = 0, blocks = 0, turnovers = 1, fouls = 1)
session.add(playerstats24)
session.commit()
