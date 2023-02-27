from .automate import getGameProps
from templates.tables import *
from templates.email import *
from tests.test import games


def getGamePropsContent():

    games = getGameProps()
    columns = ['Game', 'PlayNow', 'Sports Interact', 'Bet365', 'Pinnacle']

    moneyLinesTable = getTableHTML(titleName='Money Lines', 
                                   columnNames=columns,
                                   dataRows=getGamesHTML(games, moneyLineFormat))

    spreadsTable = getTableHTML(titleName='Spreads', 
                                columnNames=columns,
                                dataRows=getGamesHTML(games, spreadFormat))

    overUndersTable = getTableHTML(titleName='Over Unders', 
                                columnNames=columns,
                                dataRows=getGamesHTML(games, overUnderFormat))

    content = [moneyLinesTable,
               spreadsTable,
               overUndersTable,
               ]
    
    return getEmailHTML(content)