from tests.player import *
from utils.parser.player import PlayNowPlayerParser, PinnaclePlayerParser
from models.playerprop import PlayerProp
from models.allplayerprops import AllPlayerProps

'''
pinnacleGames = getPinnacleTest3()
q= PinnaclePlayerParser(pinnacleGames)
q.parseAll()''' 

pinnacleGames = getPinnacleTest3()
playNowGames = getPlayNowTest3()

playerProps = []

for bet in pinnacleGames:
    playerProp = PlayerProp('Pinnacle', bet)

    if playerProp.is_valid():
        playerProps.append(playerProp)

for bet in playNowGames:
    playerProp = PlayerProp('Play Now', bet)

    if playerProp.is_valid():
        playerProps.append(playerProp)

allProps = AllPlayerProps()
allProps.add_prop(playerProps)


for f in allProps.games:
    print(allProps.games[f][2])