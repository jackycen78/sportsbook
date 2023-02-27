from datetime import datetime

def decimalToAmerican(odds):
    if not odds:
        return ''
    if odds.startswith('+') or odds.startswith('-'):
        return odds
    
    try:
        odds = float(odds)
        if odds >= 2:
            odds = int((odds - 1) * 100)
            return f'+{odds}'
        odds = int(-100 / (odds - 1))
        return str(odds)
    except:
        return ''
    
def zipData(teams, spreads, moneyLines, overUnders):
    teamNames = ['away', 'home']
    spreadNames = ['awaySpread', 'awaySpreadOdds', 'homeSpread', 'homeSpreadOdds']
    overUnderNames = ['over', 'overOdds', 'under', 'underOdds']
    moneyLineNames = ['awayMoneyLine', 'homeMoneyLine']
    
    return [dict(zip(teamNames, teams)), \
            dict(zip(spreadNames, spreads)), \
            dict(zip(moneyLineNames, moneyLines)), \
            dict(zip(overUnderNames, overUnders)), \
           ]       

def flatten(lst):
    return [item for sublist in lst for item in sublist]

def checkAmericanOdds(odds):
    if odds.startswith('+') or odds.startswith('-'):
        return True
    return False

def getDate():
    return f'datetime.now().strftime("%B %d")'