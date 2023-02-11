from teamNames import bet365NameChanges

teamNames = ['away', 'home']
spreadNames = ['awaySpread', 'awaySpreadOdds', 'homeSpread', 'homeSpreadOdds']
overUnderNames = ['over', 'overOdds', 'under', 'underOdds']
moneyLineNames = ['awayMoneyLine', 'homeMoneyLine']

emptyLists = [['', ''],
              ['', '', '', ''],
              ['', '', '', ''],
              ['', ''],
             ]

def zipData(teams, spreads, moneyLines, overUnders):

    return dict(zip(teamNames, teams)), \
           dict(zip(spreadNames, spreads)), \
           dict(zip(overUnderNames, overUnders)), \
           dict(zip(moneyLineNames, moneyLines)) 

def PlayNowParser(data):

    teamsData, spreadsData, moneyLinesData, overUndersData = data
    teams, spreads, overUnders, moneyLines = emptyLists

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
    teams, spreads, overUnders, moneyLines = emptyLists

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


def Bet365Parser(data):

    team, spreads, overUnders, moneyLines = data

    teams = {}
    spread = {}
    moneyLine = {}
    overUnder = {}

    teams['away'] = bet365NameChanges[team[0]]
    teams['home'] = bet365NameChanges[team[1]]

    spread['awaySpread'] = spreads[0]
    spread['awaySpreadOdds'] = spreads[1]

    spread['homeSpread'] = spreads[2]
    spread['homeSpreadOdds'] = spreads[3]

    moneyLine['awayMoneyLine'] = moneyLines[0]
    moneyLine['homeMoneyLine'] = moneyLines[1]

    overUnder['over'] = overUnders[0][2:]
    overUnder['overOdds'] = overUnders[1]

    overUnder['under'] = overUnders[2][2:]
    overUnder['underOdds'] = overUnders[3]

    return teams, spread, moneyLine, overUnder
