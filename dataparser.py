from teamNames import bet365NameChanges, sportsInteractionNameChanges

teamNames = ['away', 'home']
spreadNames = ['awaySpread', 'awaySpreadOdds', 'homeSpread', 'homeSpreadOdds']
overUnderNames = ['over', 'overOdds', 'under', 'underOdds']
moneyLineNames = ['awayMoneyLine', 'homeMoneyLine']

emptyLists = [['', ''],
              ['', '', '', ''],
              ['', ''],
              ['', '', '', ''],
             ]

def zipData(teams, spreads, moneyLines, overUnders):

    return [dict(zip(teamNames, teams)), \
            dict(zip(spreadNames, spreads)), \
            dict(zip(moneyLineNames, moneyLines)), \
            dict(zip(overUnderNames, overUnders)), \
           ]       

def flatten(lst):
    return [item for sublist in lst for item in sublist]


def PlayNowParser(data):

    teamsData, spreadsData, moneyLinesData, overUndersData = data
    teams, spreads, moneyLines, overUnders = emptyLists

    if teamsData:
        teams = teamsData.text.split('\n')

    if spreadsData:
        spreads = spreadsData.text.split('\n')

    if moneyLinesData:
        moneyLinesData = moneyLinesData.text.split('\n')
        moneyLines = [moneyLinesData[1], 
                      moneyLinesData[3]]

    if overUndersData:
        overUndersData = overUndersData.text.split('\n')
        overUnders = [overUndersData[1], 
                      overUndersData[2], 
                      overUndersData[4], 
                      overUndersData[5]]

    return zipData(teams, spreads, moneyLines, overUnders)
    

def SportsInteractionParser(data):

    teamsData, spreadsData, moneyLinesData, overUndersData = data
    teams, spreads, moneyLines, overUnders = emptyLists

    if teamsData:
        teams = teamsData.text.split(' ')
        atIndex = teams.index('@')
        awayTeam = " ".join(teams[0: atIndex])
        homeTeam = " ".join(teams[atIndex + 1:])
        awayTeam = sportsInteractionNameChanges[awayTeam] if awayTeam in sportsInteractionNameChanges else awayTeam
        homeTeam = sportsInteractionNameChanges[homeTeam] if homeTeam in sportsInteractionNameChanges else homeTeam

        teams = [awayTeam,
                 homeTeam,
                ]

    if spreadsData and len(spreadsData.text.split('\n')) == 5 and 'Closed' not in spreadsData.text:
        spreads = spreadsData.text.split('\n')[1:]

    if moneyLinesData and 'Closed' not in moneyLinesData.text:
        moneyLines = moneyLinesData.text.split('\n')[1:]

    if overUndersData and 'Closed' not in overUndersData.text:
        overUnders = overUndersData.text.split('\n')[1:]
        overUnders[0] = overUnders[0][1:]
        overUnders[2] = overUnders[2][1:]

    return zipData(teams, spreads, moneyLines, overUnders)


def Bet365Parser(data):

    teamsData, spreadsData, moneyLinesData, overUndersData = data
    teams, spreads, moneyLines, overUnders = emptyLists
    
    if teamsData:
        teams = [bet365NameChanges[team] for team in teamsData.text.split('\n')]

    if spreadsData and len(spreadsData[0].text.split('\n')) == 2:
        spreads = flatten([spread.text.split('\n') for spread in spreadsData])

    if moneyLines:
        moneyLines = [ml.text for ml in moneyLinesData]
    
    if overUndersData and len(overUndersData[0].text.split('\n')) == 2:
        overUnders = flatten([ou.text.split('\n') for ou in overUndersData])
        overUnders[0] = overUnders[0][2:]
        overUnders[2] = overUnders[2][2:]

    return zipData(teams, spreads, moneyLines, overUnders)


def PinnacleParser(data):
    
    teamsData, spreadsData, moneyLinesData, overUndersData = data
    teams, spreads, moneyLines, overUnders = emptyLists

    if teamsData:
        awayTeam, homeTeam, gameTime = teamsData.text.split('\n')
        teams = [awayTeam,
                 homeTeam,
                ]

    if spreadsData:
        spreads = spreadsData.text.split('\n')

    if moneyLinesData:
        moneyLines = moneyLinesData.text.split('\n')

    if overUndersData:
        overUnders = overUndersData.text.split('\n')

    print(zipData(teams, spreads, moneyLines, overUnders))

    return zipData(teams, spreads, moneyLines, overUnders)
