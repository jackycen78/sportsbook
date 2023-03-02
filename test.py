from tests.playertest import *

propTypes = ['Player Points', 'Player Assists', 'Player Rebounds', 'Player Three Pointers', 'Player Points + Assists + Rebounds']
games = getPlayNowTest2()

for game in games:
    for bet in game:
        for type in propTypes: 
            if bet.startswith(type):
                print(bet)

