def PlayNowParser(data):

    homeTeam = {}
    awayTeam = {}
    overUnder = {}

    awayTeam['name'] = data[0]
    homeTeam['name'] = data[1]

    awayTeam['spread'] = data[2]
    awayTeam['spreadOdds'] = data[3]

    homeTeam['spread'] = data[4]
    homeTeam['spreadOdds'] = data[5]
    
    awayTeam['moneyline'] = data[7]
    homeTeam['moneyline'] = data[9]

    overUnder['over'] = data[11]
    overUnder['overOdds'] = data[12]

    overUnder['under'] = data[14]
    overUnder['underOdds'] = data[15]

    return homeTeam, awayTeam, overUnder

def SportsInteractionParser(data):

    homeTeam = {}
    awayTeam = {}
    overUnder = {}

    awayTeam['name'] = data[2]
    homeTeam['name'] = data[3]
    awayTeam['spread'] = data[5]
    awayTeam['spreadOdds'] = data[6]

    homeTeam['spread'] = data[7]
    homeTeam['spreadOdds'] = data[8]

    awayTeam['moneyline'] = data[10]
    homeTeam['moneyline'] = data[11]

    overUnder['over'] = data[13][1:]
    overUnder['overOdds'] = data[14]

    overUnder['under'] = data[15][1:]
    overUnder['underOdds'] = data[16]

    return homeTeam, awayTeam, overUnder

def Bet365Parser(teams, spreads, overUnders, moneyLines):

    homeTeam = {}
    awayTeam = {}
    overUnder = {}

    
    #print(teams, spreads, overUnders, moneyLines)

    return homeTeam, awayTeam, overUnder


"""
['Charlotte Hornets', 'Washington Wizards', '+4.0', '1.90', '-4.0', '1.90', 'Charlotte Hornets', '2.45', 
'Washington Wizards', '1.57', 'Over', '235.5', '1.90', 'Under', '235.5', '1.90', 'Today 4:10 pm', '218']

['19:05', 'Charlotte Hornets @ Washington Wizards', 'Charlotte Hornets', 'Washington Wizards', 'POINTSPREAD', 
'+4.0', '-110', '-4.0', '-110', 'MONEYLINE', '+144', '-173', 'OVER/UNDER', 'O235.5', '-112', 'U235.5', '-107']

"""

