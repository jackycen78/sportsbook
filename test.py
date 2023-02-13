from bet import *
from allbets import AllBets

"""testPlayNowBet1 = PlayNowBet([
    'Chicago Bulls',
    'Detroit Pistons',
    '+3.0',
    '1.90',
    '-3.0',
    '1.90',
    '',
    '2.30',
    '',
    '1.64',
    '',
    '235.0',
    '1.90',
    '',
    '235.0',
    '1.90',
])

testPlayNowBet2 = PlayNowBet([
    'Utah Jazz',
    'Toronto Raptors',
    '+8.0',
    '1.90',
    '-8.0',
    '1.90',
    '',
    '3.50',
    '',
    '1.31',
    '',
    '232.0',
    '1.90',
    '',
    '232.0',
    '1.90',
])

testSportsInteractionBet1 = SportsInteractionBet([
    '',
    '',
    'Chicago Bulls',
    'Detroit Pistons',
    '',
    '+3.5',
    '1.90',
    '-3.5',
    '1.90',
    '',
    '2.40',
    '1.25',
    '',
    'O236.0',
    '1.90',
    'U236.0',
    '1.90',
])

testSportsInteractionBet2 = SportsInteractionBet([
    '',
    '',
    'Utah Jazz',
    'Toronto Raptors',
    '',
    '+8.5',
    '1.90',
    '-8.5',
    '1.90',
    '',
    '3.55',
    '1.26',
    '',
    'O232.5',
    '1.90',
    'U232.5',
    '1.90',
])

testBet365Bet1 = Bet365Bet([ 
    ['CHI Bulls', 'DET Pistons'],               # Teams
    ['+2.5', '1.90', '-2.5', '1.90'],           # Spreads
    ['O 234.0', '1.91', 'U 2.34', '1.89'],      # Over Under
    ['2.30', '135'],                            # Money Line
])

testBet365Bet2 = Bet365Bet([
    ['UTA Jazz', 'TOR Raptors'],                # Teams
    ['+9.5', '1.90', '-9.5', '1.90'],           # Spreads
    ['O 232.0', '2.01', 'U 232.0', '1.79'],      # Over Under
    ['2.30', '135'],                            # Money Line
])
"""

testBet365Bet1 = Bet365Bet(['', '', '', ''])
testBet365Bet1.teams = {'home': 'UTA Jazz',
                        'away': 'TOR Raptors',
                       }

testBet365Bet1.spread = {'homeSpread' : '+9.5',
                         'homeSpreadOdds' : '1.90',
                         'awaySpread' : '-9.5',
                         'awaySpreadOdds' : '1.90',
                         }

testBet365Bet1.moneyLine = {'homeMoneyLine' : '1.36',
                            'awayMoneyLine' : '3.25',
                            }

testBet365Bet1.overUnder = {'over': '232.0',
                            'overOdds': '2.01',
                            'under': '232.0',
                            'underOdds': '1.79',
                            }

testPlayNowBet1 = PlayNowBet(['', '', '', ''])
testPlayNowBet1.teams = {'home': 'UTA Jazz',
                         'away': 'TOR Raptors',
                        }

testPlayNowBet1.spread = {'homeSpread' : '+9.0',
                          'homeSpreadOdds' : '1.90',
                          'awaySpread' : '-9.0',
                          'awaySpreadOdds' : '1.90',
                         }

testPlayNowBet1.moneyLine = {'homeMoneyLine' : '1.56',
                             'awayMoneyLine' : '2.98',
                            }

testPlayNowBet1.overUnder = {'over': '231.0',
                             'overOdds': '2.11',
                             'under': '231.0',
                             'underOdds': '1.75',
                            }


print(testPlayNowBet1)