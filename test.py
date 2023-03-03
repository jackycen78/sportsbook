from tests.player import *
from utils.parser.player import PlayNowPlayerParser

propTypes = ['Pts+Rebs+Asts', 'Points', 'Assists', 'Rebounds', '3 Point FG']


games = getPinnacleTest2()

for game in games:
    for bet in game:

        betNameStart = bet.find('(')
        betNameEnd = bet.find(')') + 1
        last = bet.rfind(')') + 1

        player = bet[:betNameStart - 1]
        type = bet[betNameStart + 1: betNameEnd - 1]
        info = bet[last:]

        if info and type in propTypes:
            info = info.split('\n')[1:]

            #if info:
            #print(f'{player} {type} {info}')

games = getPlayNowTest2()
p = PlayNowPlayerParser(games)
p.parseAll()