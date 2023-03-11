from automate.game import getGameBets
from templates.tables import *
from templates.email import *
from templates.game import createGameEmail
from templates.player import getPropsHTML
from tests.game import get_all_games
from tests.player import get_all_props
from .config import PLAYER_PROPS, PLAYER_BOOKS

def getGameBetContent():
    games = getGameBets() #get_all_games().games #get_all_games() getGameBets()
    
    return createGameEmail(games)

def getPlayerPropsContent():

    columns = ['Player', 'Prop'] + PLAYER_BOOKS
    props = get_all_props()

    content = []
    for team in props.games:
        curTeam = props.games[team]
        contentHTML = getTableHTML(title=team, 
                                   columnNames=columns,
                                   dataRows=getPropsHTML(curTeam))
        content.append(contentHTML)

    return getEmailHTML(content)
    
    