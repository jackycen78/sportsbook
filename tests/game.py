from models.allgamebets import AllBets
from models.gamebet import GameBet

PLAYNOW_FILE = 'tests/games/playnow/game.txt'
SPORTSINTERACT_FILE = 'tests/games/sportsinteract/game.txt'
PINNACLE_FILE = 'tests/games/pinnacle/game.txt'


def get_file(book):
    files = {'Play Now': PLAYNOW_FILE,
             'Sports Interact': SPORTSINTERACT_FILE,
             'Pinnacle' : PINNACLE_FILE,
            }
             
    return files[book]

def parse_book(book):
    file = get_file(book)
    with open(file) as f:
        gameData = f.readlines()

    games = []
    curStr = ''
    for line in gameData:
        if line == '\n':
            curStr = curStr[:-2]
            games.append(curStr)
            curStr = ''
        else:
            curStr += line
    return games

def create_book_bet(book):
    gameBets = []
    games = parse_book(book)

    for i in range(0, len(games), 4):
        data = [games[i],
                games[i+1],
                games[i+2],
                games[i+3],]
        gameBet = GameBet(book, data)

        gameBets.append(gameBet)
    return gameBets

