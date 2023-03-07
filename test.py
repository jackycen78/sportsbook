from models.playerprop import PlayerProp
from models.allplayerprops import AllPlayerProps
from tests.createdata import parse_game_info, parse_player_props


def create_player_props(book):
    playerProps = []
    props = parse_player_props(book)
    gameInfos = parse_game_info(book)

    for i in range(len(props)):
        prop = props[i]
        gameInfo = gameInfos[i]
        playerProp = PlayerProp(book, gameInfo, prop)
        if playerProp.is_valid():
            playerProps.append(playerProp)
    return playerProps

allProps = AllPlayerProps()
allProps.add_prop(create_player_props('Pinnacle'))
allProps.add_prop(create_player_props('Play Now'))
allProps.add_prop(create_player_props('Sports Interaction'))

print(allProps)
