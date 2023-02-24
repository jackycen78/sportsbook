def getCellHTML(text):
    outputStr =  '''
                    <td style="border-radius: 4px;
                               text-align: center;
                               width: 20%;
                               background-color: #FFFFFF;
                               padding: 0.5rem;
                               margin: 1.5px;
                              "> 
                 '''
    
    if type(text) == str:
            outputStr += f'{text} \n'
    elif type(text) == list:
        for t in text:
            outputStr += f'<br> {t} </br> \n'
    outputStr += '</td>'
    return outputStr

def getTableHTML(titleName, columnNames, dataRows):
     
    outputStr = f'''
                    <h1> {titleName} </h1>

                        <table border="3" 
                            style="background-color: #FFFFFF;
                                border:0px solid #000000;
                                border-radius: 4px;
                                width: 100%;
                                " 
                            cellpadding="10"
                            cellspacing="3"           
                        >
                            <tr>
                   '''
    
    for col in columnNames:
        outputStr += f' {getCellHTML(col)} \n'

    outputStr += f'''
                             </tr>
                            
                             {dataRows}

                        </table>
                  '''     
    
    return outputStr

def getGamesHTML(games, format):
    outputStr = ''
    for team in games:
        if len(games[team]) == 4:
            outputStr += '<tr> \n'
            curGame = games[team][0]
            outputStr += getCellHTML([curGame.get_away_city(), 
                                      'at', 
                                      curGame.get_home_city(),
                                     ])
            for bet in games[team]:
                outputStr+= getCellHTML(format(bet))
            outputStr += '</tr>'
    return outputStr


def moneyLineFormat(bet):
    format = [bet.get_away_team(),
              bet.moneyLine['awayMoneyLine'],
              bet.get_home_team(),
              bet.moneyLine['homeMoneyLine'],
              ]
    return format 

def spreadFormat(bet):
    format = [f"{bet.get_away_team()} {bet.spread['awaySpread']}",
              bet.spread['awaySpreadOdds'],
              f"{bet.get_home_team()} {bet.spread['homeSpread']}",
              bet.spread['homeSpreadOdds'],
              ]
    return format

def overUnderFormat(bet):
     format = [f"O {bet.overUnder['over']}",
               bet.overUnder['overOdds'],
               f"U {bet.overUnder['under']}", 
               bet.overUnder['underOdds'],
               ]
     return format


                            

    


'''def getHTMLDocument(tables):
     
     return 

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

            .format(moneyLines = getTableHTML(titleName='Money Lines', 
                                                 columnNames='',
                                                 dataRows=getMoneyLineHTML(games)),
                       spreads = getTableHTML('Spreads', getSpreadHTML(games)),
                       overUnders = getTableHTML('Over Unders', getOverUnderHTML(games))
                       )
'''
