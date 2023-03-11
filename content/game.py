from utils.website import Website
from automate.game import GameBets
from templates.game import createGameEmail
from tests.game import get_all_test_bets


def getGameBetContent(test=True):
    if test:
        games = get_all_test_bets().games
    
    else:
        site = Website()
        bets = GameBets(site) 
        games = bets.get_all_bets().games

    return createGameEmail(games)