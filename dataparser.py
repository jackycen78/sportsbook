from teamNames import bet365NameChanges

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
        teams = [" ".join(teams[0: atIndex]), 
                 " ".join(teams[atIndex + 1:])
                ]

    if 'Closed' not in spreadsData.text:
        spreads = spreadsData.text.split('\n')[1:]

    if 'Closed' not in moneyLinesData.text:
        moneyLines = moneyLinesData.text.split('\n')[1:]

    if 'Closed' not in overUndersData.text:
        overUnders = overUndersData.text.split('\n')[1:]
        overUnders[0] = overUnders[0][1:]

    return zipData(teams, spreads, moneyLines, overUnders)


def flatten(lst):
    return [item for sublist in lst for item in sublist]

def Bet365Parser(data):

    teamsData, spreadsData, moneyLinesData, overUndersData = data
    
    teams = [bet365NameChanges[team] for team in teamsData.text.split('\n')]
    spreads = flatten([spread.text.split('\n') for spread in spreadsData])
    moneyLines = [ml.text for ml in moneyLinesData]
    overUnders = flatten([ou.text.split('\n') for ou in overUndersData])

    """if overUnders[0]:
        overUnders[0] = overUnders[0][2:]
    if overUnders[2]:
        overUnders[2] = overUnders[2][2:]"""

    return zipData(teams, spreads, moneyLines, overUnders)
    

