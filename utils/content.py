from .automate.game import getGameProps
from templates.tables import *
from templates.email import *
from tests.test import games
from .config import SITES, GAMEPROPS

COLUMNS = ['Game'] + SITES

def getGamePropsContent():
    games = getGameProps()
    content = []

    for prop in GAMEPROPS:
        contentHTML = getTableHTML(betType=prop, 
                                   columnNames=COLUMNS,
                                   dataRows=getGamesHTML(games, prop)
                     )
        content.append(contentHTML)
    
    return getEmailHTML(content)