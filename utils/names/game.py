bet365NameChanges = {'BOS Celtics' : 'Boston Celtics',
                     'DEN Nuggets' : 'Denver Nuggets',
                     'PHI 76ers' : 'Philadelphia 76ers',
                     'CLE Cavaliers' : 'Cleveland Cavaliers',
                     'LA Lakers' : 'Los Angeles Lakers',
                     'ATL Hawks' : 'Atlanta Hawks',
                     'CHI Bulls' : 'Chicago Bulls',
                     'POR Trail Blazers' : 'Portland Trail Blazers',
                     'OKC Thunder' : 'Oklahoma City Thunder',
                     'SA Spurs' : 'San Antonio Spurs',
                     'PHX Suns' : 'Phoenix Suns',
                     'LA Clippers' : 'Los Angeles Clippers',
                     'MEM Grizzlies' : 'Memphis Grizzlies',
                     'NO Pelicans' : 'New Orleans Pelicans',
                     'SAC Kings' : 'Sacramento Kings',
                     'TOR Raptors' : 'Toronto Raptors',
                     'MIN Timberwolves' : 'Minnesota Timberwolves',
                     'UTA Jazz' : 'Utah Jazz',
                     'ORL Magic' : 'Orlando Magic',
                     'DET Pistons' : 'Detroit Pistons',
                     'MIL Bucks' : 'Milwaukee Bucks',
                     'GS Warriors' : 'Golden State Warriors',
                     'DAL Mavericks' : 'Dallas Mavericks',
                     'MIA Heat' : 'Miami Heat',
                     'BKN Nets' : 'Brooklyn Nets',
                     'NY Knicks' : 'New York Knicks',
                     'IND Pacers' : 'Indiana Pacers',
                     'WAS Wizards' : 'Washington Wizards',
                     'CHA Hornets' : 'Charlotte Hornets',   
                     'HOU Rockets' : 'Houston Rockets',
                     }

sportsIntNameChanges = {'LA Lakers': 'Los Angeles Lakers',
                        'LA Clippers': 'Los Angeles Clippers',
                        'Oklahoma City': 'Oklahoma City Thunder',
                        }

fullTeamToTeam = {'Boston Celtics' : 'Celtics',
                  'Denver Nuggets' : 'Nuggets',
                  'Philadelphia 76ers' : '76ers',
                  'Cleveland Cavaliers' : 'Cavaliers',
                  'Los Angeles Lakers' : 'Lakers',
                  'Atlanta Hawks' : 'Hawks',
                  'Chicago Bulls' : 'Bulls',
                  'Portland Trail Blazers' : 'Trail Blazers',
                  'Oklahoma City Thunder' : 'Thunder',
                  'San Antonio Spurs' : 'Spurs',
                  'Phoenix Suns' : 'Suns',
                  'Los Angeles Clippers' : 'Clippers',
                  'Memphis Grizzlies' : 'Grizzlies',
                  'New Orleans Pelicans' : 'Pelicans',
                  'Sacramento Kings' : 'Kings',
                  'Toronto Raptors' : 'Raptors',
                  'Minnesota Timberwolves' : 'Timberwolves',
                  'Utah Jazz' : 'Jazz',
                  'Orlando Magic' : 'Magic',
                  'Detroit Pistons' : 'Pistons',
                  'Milwaukee Bucks' : 'Bucks',
                  'Golden State Warriors' : 'Warriors',
                  'Dallas Mavericks' : 'Mavericks',
                  'Miami Heat' : 'Heat',
                  'Brooklyn Nets' : 'Nets',
                  'New York Knicks' : 'Knicks',
                  'Indiana Pacers' : 'Pacers',
                  'Washington Wizards' : 'Wizards',
                  'Charlotte Hornets' : 'Hornets',   
                  'Houston Rockets' : 'Rockets',
                  }

fullTeamToCity = {'Atlanta Hawks' : 'Atlanta',
                  'Boston Celtics' : 'Boston',
                  'Brooklyn Nets' : 'Brooklyn',
                  'Charlotte Hornets' : 'Charlotte',   
                  'Dallas Mavericks' : 'Dallas',
                  'Denver Nuggets' : 'Denver',
                  'Detroit Pistons' : 'Detroit',
                  'Golden State Warriors' : 'Golden State',
                  'Houston Rockets' : 'Houston',
                  'Indiana Pacers' : 'Indiana',
                  'Los Angeles Clippers' : 'Los Angeles',
                  'Los Angeles Lakers' : 'Los Angeles',
                  'Memphis Grizzlies' : 'Grizzlies',
                  'Miami Heat' : 'Miami',
                  'Milwaukee Bucks' : 'Milwaukee',
                  'Minnesota Timberwolves' : 'Minnesota',
                  'New Orleans Pelicans' : 'New Orleans',
                  'New York Knicks' : 'New York',
                  'Oklahoma City Thunder' : 'Oklahoma City',
                  'Orlando Magic' : 'Orlando',
                  'Philadelphia 76ers' : 'Philadelphia',
                  'Phoenix Suns' : 'Phoenix',
                  'Portland Trail Blazers' : 'Portland',
                  'Sacramento Kings' : 'Sacramento',
                  'San Antonio Spurs' : 'San Antonio',
                  'Toronto Raptors' : 'Toronto',
                  'Utah Jazz' : 'Utah',
                  'Washington Wizards' : 'Washington',
                 }


def getBet365TeamName(name):
    if name in bet365NameChanges:
        return bet365NameChanges[name]
    return name

def getSportsIntTeamName(name):
    if name in sportsIntNameChanges:
        return sportsIntNameChanges[name]
    return name

def getCityName(name):
    if name != 'Portland Trail Blazers':
        space = name.rfind(' ')
        return name[:space]
    else:
        return 'Portland'

def getTeamName(name):
    if name != 'Portland Trail Blazers':
        space = name.rfind(' ')
        return name[space + 1:]
    else:
        return 'Trail Blazers'

