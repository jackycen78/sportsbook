from templates.tables import *
#from main import games
from test import games

columns = ['Game', 'PlayNow', 'Sports Interact', 'Bet365', 'Pinnacle']

template = """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>

                <body>
                    {moneyLines}
                    {spreads}
                    {overUnders}
                </body>
            </html>
            """.format(moneyLines = getTableHTML(titleName='Money Lines', 
                                                 columnNames=columns,
                                                 dataRows=getGamesHTML(games, moneyLineFormat)),
                       spreads = getTableHTML(titleName='Spreads', 
                                                 columnNames=columns,
                                                 dataRows=getGamesHTML(games, spreadFormat)),
                       overUnders = getTableHTML(titleName='Over Unders', 
                                                 columnNames=columns,
                                                 dataRows=getGamesHTML(games, overUnderFormat)),
                       )



