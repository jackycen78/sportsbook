from teamNames import bet365NameChanges

def PlayNowParser(data):

    
    spread = {}
    moneyLine = {}
    overUnder = {}

    awayTeam = data[0]
    homeTeam = data[1]

    spread['awaySpread'] = data[2]
    spread['awaySpreadOdds'] = data[3]

    spread['homeSpread'] = data[4]
    spread['homeSpreadOdds'] = data[5]
    
    moneyLine['awayMoneyLine'] = data[7]
    moneyLine['homeMoneyLine'] = data[9]

    overUnder['over'] = data[11]
    overUnder['overOdds'] = data[12]

    overUnder['under'] = data[14]
    overUnder['underOdds'] = data[15]

    return homeTeam, awayTeam, spread, moneyLine, overUnder

def SportsInteractionParser(data):

    spread = {}
    moneyLine = {}
    overUnder = {}

    awayTeam = data[2]
    homeTeam = data[3]

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

    return homeTeam, awayTeam, spread, moneyLine, overUnder

def Bet365Parser(data):

    teams, spreads, overUnders, moneyLines = data

    spread = {}
    moneyLine = {}
    overUnder = {}

    awayTeam = bet365NameChanges[teams[0]]
    homeTeam = bet365NameChanges[teams[1]]

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

    return homeTeam, awayTeam, spread, moneyLine, overUnder
