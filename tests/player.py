from models.allplayerprops import AllPlayerProps
from models.playerprop import PlayerProp
from utils.config import PLAYER_BOOKS

PINNACLE_PLAYERFILE = 'tests/props/pinnacle/prop.txt'
PINNACLE_GAMEFILE = 'tests/props/pinnacle/gameinfo.txt'
PLAYNOW_PLAYERFILE = 'tests/props/playnow/prop.txt'
PLAYNOW_GAMEFILE = 'tests/props/playnow/gameinfo.txt'
SPORTSINTERACT_PLAYERFILE = 'tests/props/sportsinteract/prop.txt'
SPORTSINTERACT_GAMEFILE = 'tests/props/sportsinteract/gameinfo.txt'

def get_file(book, type):
    files = {'Pinnacle': {'Player': PINNACLE_PLAYERFILE,
                          'Game': PINNACLE_GAMEFILE,
                          },
             'Play Now': {'Player': PLAYNOW_PLAYERFILE,
                          'Game': PLAYNOW_GAMEFILE,
                          },
             'Sports Interact': {'Player': SPORTSINTERACT_PLAYERFILE,
                                    'Game': SPORTSINTERACT_GAMEFILE,
                                    },
                         }
    return files[book][type]


def parse_player_props(book):
    file = get_file(book, 'Player')

    with open(file) as f:
        playerData = f.readlines()
    lst = []
    curStr = ''
    for line in playerData:
        if line == ' \n':
            curStr = curStr[:-2]
            lst.append(curStr)
            curStr = ''
        else:
            curStr += line
    return lst

def parse_game_info(book):
    file = get_file(book, 'Game')
    with open(file) as f:
        gameData = f.readlines()
    lst = []
    curStr = ''
    for line in gameData:
        if line == ' \n':
            curStr = curStr[:-1]
            lst.append(curStr)
            curStr = ''
        else:
            curStr += line
    return lst

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

def get_all_test_props():
    allProps = AllPlayerProps()
    for book in PLAYER_BOOKS:
        allProps.add_prop(create_player_props(book))
    return allProps