from tests.player import *
from utils.parser.player import PlayNowPlayerParser, PinnaclePlayerParser
from models.playerprop import PlayerProp
from models.allplayerprops import AllPlayerProps

pinProps = getPinnaclePlayerProps()
pinGameInfo = getPinnacleGameInfo()

playProps = getPlayNowPlayerProps()
playGameInfo = getPlayNowPlayerProps()

playerProps = []

for i in range(len(pinProps)):
    prop = pinProps[i]
    gameInfo = pinGameInfo[i]

    playerProp = PlayerProp('Pinnacle', gameInfo, prop)
    if playerProp.is_valid():
        playerProps.append(playerProp)

for i in range(len(playProps)):
    prop = playProps[i]
    gameInfo = playGameInfo[i]
    playerProp = PlayerProp('Play Now', gameInfo, prop)

    if playerProp.is_valid():
        playerProps.append(playerProp)

allProps = AllPlayerProps()
allProps.add_prop(playerProps)


print(allProps)