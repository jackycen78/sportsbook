from bet import *
from allbets import AllBets
import pandas as pd

testPlayNowBet1 = PlayNowBet([
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



allBets = AllBets()
allBets.addBet([testBet365Bet1, testBet365Bet2, testPlayNowBet1, testPlayNowBet2, testSportsInteractionBet1, testSportsInteractionBet2])


df = pd.DataFrame([x.get_teams() | x.overUnder for x in allBets.betlist])

df.sort_values(by='Teams')

print(df)