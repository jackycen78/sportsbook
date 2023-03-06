from .automate.game import getGameBets
from templates.tables import *
from templates.email import *
from tests.game import games
from .config import GAME_BETS, GAME_SITES, PLAYER_PROPS, PLAYER_SITES

def getGameBetContent():
    columns = ['Game'] + GAME_SITES
    #games = getGameProps()
    content = []
    for prop in GAME_BETS:
        contentHTML = getTableHTML(betType=prop, 
                                   columnNames=columns,
                                   dataRows=getGamesHTML(games, prop)
                     )
        content.append(contentHTML)
    return getEmailHTML(content)

def getPlayerPropsContent():

    pass 