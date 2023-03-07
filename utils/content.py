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
        contentHTML = getTableHTML(betType=game, 
                                   columnNames=columns,
                                   dataRows=getGamesHTML(games, game)
                     )
        content.append(contentHTML)
    return getEmailHTML(content)

def getPlayerPropsContent():

    columns = ['Player', 'Prop'] + PLAYER_SITES
    props = get_all_props()

    for team in props.games:
    
        curTeam = props.games[team]

        for player in curTeam:
            curPlayer = curTeam[player]

            for type in curPlayer:
                curType = curPlayer[type]

                for prop in curType:
                    print(f'{prop.player}')
                #print(prop)    
    
    