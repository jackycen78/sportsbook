from datetime import datetime

def decimal_to_american(odds):
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
    
def zip_data(teams, spreads, moneyLines, overUnders):
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

def capitialize_first_letter(string):
    words = string.split(' ')
    for i, word in enumerate(words):
        words[i] = word[0].upper() + word[1:].lower()
    return ' '.join(words)

def get_date():
    month = datetime.now().strftime("%B")
    day = datetime.now().strftime("%d")
    if day.startswith('0'):
        day = day[1]

    return f'{month} {day}'

def write_file(path, content):
    file = open(path, 'a')
    file.write(content)

def clear_file(path):
    open(path, 'w').close()

def clear_tests(book):
    
    files = ['prop', 'gameinfo']
    for file in files:
        path = f'tests/props/{book}/{file}.txt'
        clear_file(path)
