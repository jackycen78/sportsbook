from teamNames import bet365NameChanges

teamNames = ['away', 'home']
spreadNames = ['awaySpread', 'awaySpreadOdds', 'homeSpread', 'homeSpreadOdds']
overUnderNames = ['over', 'overOdds', 'under', 'underOdds']
moneyLineNames = ['awayMoneyLine', 'homeMoneyLine']

emptyTeams = ['', '']
emptySpreads = ['', '', '', '']
emmptyOverUnders = ['', '', '', '']
emptyMoneyLines = ['', '']

def PlayNowParser(data):

    teams, spreads, moneyLines, overUnders = data
    
    if teams:
        teams = teams.text.split('\n')
    else:
        teams = emptyTeams

    if spreads:
        spreads = spreads.text.split('\n')
    else:
        spreads = emptySpreads

    if moneyLines:
        moneyLines = moneyLines.text.split('\n')
        moneyLines = [moneyLines[1], moneyLines[3]]
    else:
        moneyLines = emptyMoneyLines

    if overUnders:
        overUnders = overUnders.text.split('\n')
        overUnders = [overUnders[1], overUnders[2], overUnders[4], overUnders[5]]
    else:
        overUnders = emmptyOverUnders

    return dict(zip(teamNames, teams)), \
           dict(zip(spreadNames, spreads)), \
           dict(zip(overUnderNames, overUnders)), \
           dict(zip(moneyLineNames, moneyLines)) 

def SportsInteractionParser(data):

    teams = {}
    spread = {}
    moneyLine = {}
    overUnder = {}

    teams['away'] = data[2]
    teams['home'] = data[3]

    spread['awaySpread'] = data[5]
    spread['awaySpreadOdds'] = data[6]

    spread['homeSpread'] = data[7]
    spread['homeSpreadOdds'] = data[8]

    moneyLine['awayMoneyLine'] = data[10]
    moneyLine['homeMoneyLine'] = data[11]

    overUnder['over'] = data[13][1:]
    overUnder['overOdds'] = data[14]

    overUnder['under'] = data[15][1:]
    overUnder['underOdds'] = data[16]

    return teams, spread, moneyLine, overUnder

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
