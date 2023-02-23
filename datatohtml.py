def getMoneyLineHTML(games):
    outputStr = ''
    for team in games:
        if len(games[team]) == 4:
                curTeam = games[team][0]
                outputStr += '<tr> \n'
                outputStr += getCellHTML([curTeam.get_away_city(), 'at', curTeam.get_home_city()])

                for bet in games[team]:
                    outputStr+= getCellHTML([bet.get_away_team(),
                                             bet.moneyLine['awayMoneyLine'],
                                             bet.get_home_team(),
                                             bet.moneyLine['homeMoneyLine'],
                                             ])
                outputStr += '</tr>'
    return outputStr


def getSpreadHTML(games):
    outputStr = ''
    for team in games:
        if len(games[team]) == 4:
                curTeam = games[team][0]
                outputStr += '<tr> \n'
                outputStr += getCellHTML([curTeam.get_away_city(), 'at', curTeam.get_home_city()])

                for bet in games[team]:
                    outputStr+= getCellHTML([f"{bet.get_away_team()} {bet.spread['awaySpread']}",
                                                bet.spread['awaySpreadOdds'],
                                             f"{bet.get_home_team()} {bet.spread['homeSpread']}",
                                                bet.spread['homeSpreadOdds'],
                                             ])
                outputStr += '</tr>'
    return outputStr
    
def getOverUnderHTML(games):
    outputStr = ''
    for team in games:
        if len(games[team]) == 4:
                curTeam = games[team][0]
                outputStr += '<tr> \n'
                outputStr += getCellHTML([curTeam.get_away_city(), 'at', curTeam.get_home_city()])

                for bet in games[team]:
                    outputStr+= getCellHTML([f"O {bet.overUnder['over']} {bet.overUnder['overOdds']}",
                                             f"U {bet.overUnder['under']} {bet.overUnder['underOdds']}",
                                             ])
                outputStr += '</tr>'
    return outputStr
    

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
    else:
        for t in text:
            outputStr += f'<br> {t} </br> \n'
    outputStr += '</td>'

    return outputStr


def getTableHTML(titleName, dataRows):
     
     return '''
                <h1> {title} </h1>

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
                            {col1}
                            {col2}
                            {col3}
                            {col4}
                            {col5}
                        </tr>

                        {data}

                    </table>

            '''.format(title=titleName,
                       col1 = getCellHTML('Game'),
                       col2 = getCellHTML('PlayNow'),
                       col3 = getCellHTML('Sports Interact'),
                       col4 = getCellHTML('Bet365'),
                       col5 = getCellHTML('Pinnacle'),
                       data=dataRows,
                       )
