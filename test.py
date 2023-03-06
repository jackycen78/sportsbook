from models.playerprop import PlayerProp
from models.allplayerprops import AllPlayerProps
from tests.createdata import create_game_info, create_player_props

playerProps = []
SportsInteractionProps = create_player_props('Sports Interaction')
SportsInteractionGameInfo = create_game_info('Sports Interaction')

pinnaclePlayerProps = create_player_props('Pinnacle')
pinnacleGameInfo = create_game_info('Pinnacle')

playNowPlayerProps = create_player_props('Play Now')
playNowGameInfo = create_game_info('Play Now')


for i in range(len(SportsInteractionProps)):
    prop = SportsInteractionProps[i]
    gameInfo = SportsInteractionGameInfo[i]

    playerProp = PlayerProp('Sports Interaction', gameInfo, prop)
    if playerProp.is_valid():
        playerProps.append(playerProp)


for i in range(len(pinnaclePlayerProps)):
    prop = pinnaclePlayerProps[i]
    gameInfo = pinnacleGameInfo[i]

    playerProp = PlayerProp('Pinnacle', gameInfo, prop)
    if playerProp.is_valid():
        playerProps.append(playerProp)

for i in range(len(playNowPlayerProps)):
    prop = playNowPlayerProps[i]
    gameInfo = playNowGameInfo[i]
    playerProp = PlayerProp('Play Now', gameInfo, prop)

    if playerProp.is_valid():
        playerProps.append(playerProp)

allProps = AllPlayerProps()
allProps.add_prop(playerProps)

print(allProps)
