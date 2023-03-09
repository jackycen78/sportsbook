from .automate.game import getGameBets
from templates.tables import *
from templates.email import *
from tests.game import get_all_games
from tests.player import get_all_props
from .config import GAME_BETS, GAME_SITES, PLAYER_PROPS, PLAYER_SITES

def getGameBetContent():
    columns = ['Game'] + GAME_SITES
    games = getGameBets() #get_all_games() getGameBets()
    content = []
    for game in GAME_BETS:
        contentHTML = getTableHTML(title=game, 
                                   columnNames=columns,
                                   dataRows=getGamesHTML(games, game)
                     )
        content.append(contentHTML)
    return getEmailHTML(content)

def getPlayerPropsContent():

    columns = ['Player', 'Prop'] + PLAYER_SITES
    props = get_all_props()

    content = []
    for team in props.games:
        curTeam = props.games[team]
        contentHTML = getTableHTML(title=team, 
                                   columnNames=columns,
                                   dataRows=getPropsHTML(curTeam))
        content.append(contentHTML)

    return getEmailHTML(content)
    
    