from utils.helper import capitialize_first_letter

playNowPlayerNames = {
                    # Bucks
                    'B. Lopez': 'Brook Lopez',
                    'G. Allen': 'Grayson Allen',
                    'G. Antetokounmpo': 'Giannis Antetokounmpo',
                    'Jrue Holiday': 'Jrue Holiday',
                    'K. Middleton': 'Khris Middleton',
                    'P. Connaughton': 'Pat Connaughton',
                    'B. Portis': 'Bobby Portis',
                    'J. Crowder': 'Jae Crowder',
                    'J. Ingles': 'Joe Ingles',

                    # Sixers
                    'J. Embiid': 'Joel Embiid',
                    'J. Harden': 'James Harden',
                    'P.J. Tucker': 'PJ Tucker',
                    'T. Harris': 'Tobias Harris',
                    'T. Maxey': 'Tyrese Maxey',
                    'D. Melton': "De'Anthony Melton",

                    # Kings
                    'D. Fox': "De'Aaron Fox",
                    'D. Sabonis': 'Domantas Sabonis',
                    'H. Barnes': 'Harrison Barnes',
                    'K. Huerter': 'Kevin Huerter',
                    'M. Monk': 'Malik Monk',
                    'Keegan Murray': 'Keegan Murray',

                    # Timberwolves
                    'A. Edwards': 'Anthony Edwards',
                    'Jaden McDaniels': 'Jaden McDaniels',
                    'K. Anderson': 'Kyle Anderson',
                    'M. Conley': 'Mike Conley',
                    'R. Gobert': 'Rudy Gobert',
                    'N. Reid': 'Naz Reid',
                    'N. Alexander-Walker': 'Nickeil Alexander-Walker',
                    'T. Prince': 'Taurean Prince',

                    # Magic
                    'G. Harris': 'Gary Harris',
                    'M. Fultz': 'Markelle Fultz',
                    'W. Carter Jr.': 'Wendell Carter Jr.',
                    'Franz Wagner': 'Franz Wagner',
                    'Paolo Banchero': 'Paolo Banchero',

                    # Hornets
                    'G. Hayward': 'Gordon Hayward',
                    'K. Oubre Jr.': 'Kelly Oubre Jr.',
                    'T. Rozier': 'Terry Rozier',
                    'Mark Williams': 'Mark Williams',
                    'P.J. Washington': 'P.J Washington',
                    'D. Smith Jr.': 'Dennis Smith Jr.',
                    'N. Richards': 'Nick Richards',
                    
                    # Celtics
                    'A. Horford': 'Al Horford',
                    'J. Brown': 'Jaylen Brown',
                    'J. Tatum': 'Jayson Tatum',
                    'M. Smart': 'Marcus Smart',
                    'R. Williams III': 'Robert Williams',
                    'D. White': 'Derrick White',
                    'M. Brogdon': 'Malcolm Brogdon',
                    'G. Williams': 'Grant Williams',

                    # Nets
                    'D. Finney-Smith': 'Dorian Finney-Smith',
                    'N. Claxton': 'Nicolas Claxton',
                    'S. Dinwiddie': 'Spencer Dinwiddie',
                    'C. Johnson': 'Cameron Johnson',
                    'Mikal Bridges': 'Mikal Bridges',
                    "R. O'Neale": "Royce O'Neale",

                    # Hawks
                    'C. Capela': 'Clint Capela',
                    'D. Hunter': "De'Andre Hunter",
                    'D. Murray': 'Dejounte Murray',
                    'Trae Young': 'Trae Young',
                    'J. Collins': 'John Collins', 
                    'O. Okongwu': 'Onyeka Okongwu',
                    'S. Bey': 'Saddiq Bey',

                    # Trailblazers
                    'D. Eubanks': 'Drew Eubanks',
                    'D. Lillard': 'Damian Lillard',
                    'J. Grant': 'Jerami Grant',
                    'M. Thybulle': 'Matisse Thybulle',
                    'C. Reddish': 'Cam Reddish',
                    'N. Little': 'Nassir Little',
                    'J. Nurkic': 'Jusuf Nurkic',

                    # Heat
                    'B. Adebayo': 'Bam Adebayo',
                    'T. Herro': 'Tyler Herro',
                    'J. Butler': 'Jimmy Butler',
                    'M. Strus': 'Max Strus',
                    'V. Oladipo': 'Victor Oladipo',
                    'G. Vincent': 'Gabe Vincent',
                    'K. Love': 'Kevin Love',


                    # Knicks
                    'I. Quickley': 'Immanuel Quickley',
                    'J. Hart': 'Josh Hart',
                    'J. Brunson': 'Jalen Brunson',
                    'J. Randle': 'Julius Randle',
                    'M. Robinson': 'Mitchell Robinson',
                    'R.J. Barrett': 'RJ Barrett',
                    'Quentin Grimes': 'Quentin Grimes',

                    # Bulls
                    'A. Caruso': 'Alex Caruso',
                    'D. DeRozan': 'DeMar DeRozan',
                    'N. Vucevic': 'Nikola Vucevic',
                    'P. Beverley': 'Patrick Beverley',
                    'Z. LaVine': 'Zach LaVine',
                    'C. White': 'Coby White',
                    'P. Williams': 'Patrick Williams',

                    # Suns
                    'C. Paul': 'Chris Paul',
                    'D. Ayton': 'Deandre Ayton',
                    'D. Booker': 'Devin Booker',
                    'K. Durant': 'Kevin Durant',
                    'J. Okogie': 'Josh Okogie',
                    'C. Payne': 'Cameron Payne',
                    'T. Craig': 'Torrey Craig',
                    'T. Lyles': 'Trey Lyles',

                    # Jazz
                    'K. Olynyk': 'Kelly Olynyk',
                    'L. Markkanen': 'Lauri Markkanen',
                    'T. Horton-Tucker': 'Talen Horton-Tucker',
                    'Walker Kessler': 'Walker Kessler',
                    'J. Clarkson': 'Jordan Clarkson',
                    'K. Dunn': 'Kris Dunn',

                    # Thunder
                    'L. Dort': 'Luguentz Dort',
                    'Jalen Williams': 'Jalen Williams',
                    'Josh Giddey': 'Josh Giddey',
                    'S. Gilgeous-Alexander': 'Shai Gilgeous-Alexander',
                    'I. Joe': 'Isaiah Joe',
                    
                    # Nuggets
                    'A. Gordon': 'Aaron Gordon',
                    'J. Murray': 'Jamal Murray',
                    'K. Caldwell-Pope': 'Kentavious Caldwell-Pope',
                    'M. Porter Jr.': 'Michael Porter Jr.',
                    'N. Jokic': 'Nikola Jokic',
                    'R. Jackson': 'Reggie Jackson',

                    # Grizzlies
                    'D. Bane': 'Desmond Bane',
                    'D. Brooks': 'Dillon Brooks',
                    'J. Jackson Jr.': 'Jaren Jackson Jr.',
                    'J. Morant': 'Ja Morant',
                    'X. Tillman Sr.': 'Xavier Tillman',
                    'S. Aldama': 'Santi Aldama',
                    'L. Kennard': 'Luke Kennard',
                    'J. Konchar': 'John Konchar',

                    # Pelicans
                    'B. Ingram': 'Brandon Ingram',
                    'CJ. McCollum': 'CJ McCollum',
                    'Herb Jones': 'Herbert Jones',
                    'J. Valanciunas': 'Jonas Valanciunas',
                    'N. Marshall': 'Naji Marshall',
                    
                    # Warriors
                    'J. Poole': 'Jordan Poole',
                    'K. Looney': 'Kevon Looney',
                    'K. Thompson': 'Klay Thompson',
                    'Draymond Green': 'Draymond Green',
                    'Stephen Curry': 'Stephen Curry',
                    'D. DiVincenzo': 'Donte DiVincenzo',
    
                    # Lakers
                    'A. Davis': 'Anthony Davis',                  
                    'D. Schröder': 'Dennis Schroder',
                    'Malik Beasley': 'Malik Beasley',
                    'J. Vanderbilt': 'Jarred Vanderbilt',
                    'R. Hachimura': 'Rui Hachimura',
                    'D. Russell': "D'Angelo Russell",

                    # Clippers
                    'P. George': 'Paul George',
                    'K. Leonard': 'Kawhi Leonard',
                    'I. Zubac': 'Ivica Zubac',
                    'R. Westbrook': 'Russell Westbrook',
                    'Marcus Morris': 'Marcus Morris Sr.',
                    'E. Gordon': 'Eric Gordon',

                    # Mavericks
                    'D. Powell': 'Dwight Powell',
                    'K. Irving': 'Kyrie Irving',
                    'L. Doncic': 'Luka Doncic',
                    'R. Bullock': 'Reggie Bullock',
                    'C. Wood': 'Christian Wood',
                    'T. Hardaway Jr.': 'Tim Hardaway Jr.',

                    # Raptors
                    'F. VanVleet': 'Fred VanVleet',
                    'G. Trent Jr.': 'Gary Trent Jr.',
                    'J. Poeltl': 'Jakob Poeltl',
                    'P. Siakam': 'Pascal Siakam',
                    'O.G. Anunoby': 'OG Anunoby',
                    'P. Achiuwa': 'Precious Achiuwa',
                    'C. Boucher': 'Chris Boucher',

                    # Cavaliers
                    'D. Garland': 'Darius Garland',
                    'I. Okoro': 'Isaac Okoro',
                    'J. Allen': 'Jarrett Allen',
                    'C. LeVert': 'Caris LeVert',
                    'D. Mitchell': 'Donovan Mitchell',

                    # Pacers
                    'M. Turner': 'Myles Turner',
                    'B. Hield': 'Buddy Hield',
                    'T. Haliburton': 'Tyrese Haliburton',
                    'A. Nesmith': 'Aaron Nesmith',

                    # Rockets
                    'K. Porter Jr.': 'Kevin Porter Jr.',
                    'K. Martin Jr.': 'KJ Martin',
                    'J. Green': 'Jalen Green',
                    'Jabari Smith Jr.': 'Jabari Smith Jr.',
                    'A. Sengün': 'Alperen Sengun',
                    
                    # Wizards
                    'B. Beal': 'Bradley Beal',
                    'D. Gafford': 'Daniel Gafford',
                    'D. Wright': 'Delon Wright',
                    'K. Porzingis': 'Kristaps Porzingis',
                    'K. Kuzma': 'Kyle Kuzma',
                    'D. Avdija': 'Deni Avdija',

                    # Pistons
                    'M. Bagley III': 'Marvin Bagley III',
                    'Isiah Livers': 'Isiah Livers',
                    'Jaden Ivey': 'Jaden Ivey',
                    'J. Wiseman': 'James Wiseman',
                    'K. Hayes': 'Killian Hayes',
                    'P.J. Washington': 'PJ Washington',
                    'R.J. Hampton': 'RJ Hampton',

                    # Spurs
                    'Z. Collins': 'Zach Collins',
                    'K. Johnson': 'Keldon Johnson',
                    'D. Vassell': 'Devin Vassell',
                    }

sportsInteractPlayerNames = {'Michael Porter': 'Michael Porter Jr.',
                             'Fred Vanvleet': 'Fred VanVleet',
                             'Og Anunoby': 'OG Anunoby',
                             'Kentavious Caldwell-pope': 'Kentavious Caldwell-Pope',
                             "De'andre Hunter": "De'Andre Hunter", 
                             'Kelly Oubre': 'Kelly Oubre Jr.',
                             'P.j. Washington': 'PJ Washington',    
                             'Zach Lavine': 'Zach LaVine',
                             'Demar Derozan': 'DeMar DeRozan',     
                             'Kenyon Martin': 'KJ Martin',
                             'Jabari Smith': 'Jabari Smith Jr.',           
                             'Shai Gilgeous-alexander': 'Shai Gilgeous-Alexander',     
                             'Trey Murphy Iii': 'Trey Murphy III',
                             'Cj Mccollum': 'CJ McCollum',
                             "De'aaron Fox": "De'Aaron Fox",
                            }

pinnaclePlayerNames = {'R.J. Hampton': 'RJ Hampton',
                       'Jabari Smith Jr': 'Jabari Smith Jr.',}

teamToFullTeam = {'76ers': 'Philadelphia 76ers',
                  '76er': 'Philadelphia 76ers',
                  'Bucks': 'Milwaukee Bucks',
                  'Bulls': 'Chicago Bulls',
                  'Cavaliers': 'Cleveland Cavaliers',
                  'Celtics': 'Boston Celtics',
                  'Clippers': 'Los Angeles Clippers',
                  'Grizzlies': 'Memphis Grizzlies',
                  'Hawks': 'Atlanta Hawks',
                  'Heat': 'Miami Heat',
                  'Hornets': 'Charlotte Hornets',
                  'Jazz': 'Utah Jazz',
                  'Kings': 'Sacramento Kings',
                  'Knicks': 'New York Knicks',
                  'Lakers': 'Los Angeles Lakers',
                  'Magic': 'Orlando Magic',
                  'Mavericks': 'Dallas Mavericks',
                  'Nets': 'Brooklyn Nets',
                  'Nuggets': 'Denver Nuggets',
                  'Pacers': 'Indiana Pacers',
                  'Pelicans': 'New Orleans Pelicans',
                  'Pistons': 'Detroit Pistons',
                  'Raptors': 'Toronto Raptors',
                  'Rockets': 'Houston Rockets',
                  'Spurs': 'San Antonio Spurs',
                  'Suns': 'Phoenix Suns',
                  'Thunder': 'Oklahoma City Thunder',
                  'Timberwolves': 'Minnesota Timberwolves',
                  'Trail Blazers': 'Portland Trail Blazers',
                  'Warriors': 'Golden State Warriors',
                  'Wizards': 'Washington Wizards',
                 }

def getFullTeam(name):
    if name in teamToFullTeam:
        return teamToFullTeam[name]
    return name

def getPlayNowPlayerName(name):
    if name in playNowPlayerNames:
        return playNowPlayerNames[name]
    return name

def getSportsInteractPlayerName(name):
    name = capitialize_first_letter(name)
    if name in sportsInteractPlayerNames:
        return sportsInteractPlayerNames[name]
    return name

def getPinnaclePlayerName(name):
    if name in pinnaclePlayerNames:
        return pinnaclePlayerNames[name]
    return name