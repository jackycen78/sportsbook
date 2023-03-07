PINNACLE_PLAYERFILE = 'tests/pinnacle/prop.txt'
PINNACLE_GAMEFILE = 'tests/pinnacle/gameinfo.txt'
PLAYNOW_PLAYERFILE = 'tests/playnow/prop.txt'
PLAYNOW_GAMEFILE = 'tests/playnow/gameinfo.txt'
SPORTSINTERACTION_PLAYERFILE = 'tests/sportsinteraction/prop.txt'
SPORTSINTERACTION_GAMEFILE = 'tests/sportsinteraction/gameinfo.txt'

def get_file(book, type):
    files = {'Pinnacle': {'Player': PINNACLE_PLAYERFILE,
                          'Game': PINNACLE_GAMEFILE,
                          },
             'Play Now': {'Player': PLAYNOW_PLAYERFILE,
                          'Game': PLAYNOW_GAMEFILE,
                          },
             'Sports Interaction': {'Player': SPORTSINTERACTION_PLAYERFILE,
                                    'Game': SPORTSINTERACTION_GAMEFILE,
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
            curStr = curStr[:-3]
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
            curStr = curStr[:-2]
            lst.append(curStr)
            curStr = ''
        else:
            curStr += line
    return lst