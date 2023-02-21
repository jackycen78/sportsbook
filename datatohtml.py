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

    if type(text) == str:
        return f'''
                <td style="border-radius: 4px;
                        text-align: center;
                        width: 20%;
                        "> 
                        {text}
                </td>
                '''
    
    elif type(text) == list:
        outputStr =  '''
                        <td style="border-radius: 4px;
                                   text-align: center;
                                   width: 20%;
                                   "> 
                     '''
        for t in text:
            outputStr += f'<br> {t} </br> \n'

        outputStr += '</td>'

        return outputStr
