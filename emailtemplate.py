from datatohtml import getMoneyLineHTML, getSpreadHTML, getOverUnderHTML, getCellHTML
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

            <body  style="background-color: #FFFFFF;
                         ">
                <h1> Money Lines </h1>
                    <table border="3" 
                        style="background-color: #FFFFFF;
                            border:1.5px solid #000000;
                            border-radius: 4px;
                            width:100%;
                            " 
                        cellpadding="10"
                        cellspacing="3"           
                    >
                        <tr>
                            {col1}
                            {col2}
                            {col3}
                            {col4}
                        </tr>
                        {moneyLines}
                    </table>

                <h1> Spreads </h1>
                    <table border="3" 
                        style="background-color: #FFFFFF;
                            border:1.5px solid #000000;
                            border-radius: 4px;
                            width:100%;
                            " 
                        cellpadding="10"
                        cellspacing="3"           
                    >
                        <tr>
                            {col1}
                            {col2}
                            {col3}
                            {col4}
                        </tr>
                        {spreads}
                    </table>

                <h1> Over/Unders </h1>
                    <table border="3" 
                        style="background-color: #FFFFFF;
                            border:1.5px solid #000000;
                            border-radius: 4px;
                            width:100%;
                            " 
                        cellpadding="10"
                        cellspacing="3"           
                    >
                        <tr>
                            {col1}
                            {col2}
                            {col3}
                            {col4}
                        </tr>
                        {overUnders}
                    </table>

            </body>
            </html>
            """.format(col1 = getCellHTML('Game'),
                       col2 = getCellHTML('PlayNow'),
                       col3 = getCellHTML('Sports Interaction'),
                       col4 = getCellHTML('Bet365'),
                       moneyLines = getMoneyLineHTML(games),
                       spreads = getSpreadHTML(games),
                       overUnders = getOverUnderHTML(games),
                       )



