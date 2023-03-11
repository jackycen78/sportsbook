from models.allgamebets import AllBets
from models.gamebet import GameBet
from utils.config import GAME_BOOKS

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
            curStr = curStr[:-1]
            if curStr:
                games.append(curStr)
            curStr = ''
        elif line == 'HANDICAP\n' or line == 'MONEY LINE\n' or line == 'OVER\n' or line=='UNDER\n':
            pass
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
                games[i+3],
                ]
        gameBet = GameBet(book, data)

        gameBets.append(gameBet)
    return gameBets

def get_all_test_bets():
    
    allBets = AllBets()
    for book in GAME_BOOKS:
        allBets.add_bets(create_book_bet(book))
    return allBets