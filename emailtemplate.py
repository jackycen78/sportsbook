from datatohtml import *
from main import games
#from test import games

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
            """.format(moneyLines = getTableHTML('Money Lines', getMoneyLineHTML(games)),
                       spreads = getTableHTML('Spreads', getSpreadHTML(games)),
                       overUnders = getTableHTML('Over Unders', getOverUnderHTML(games))
                       )



