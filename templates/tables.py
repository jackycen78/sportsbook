def getCellHTML(text, size):
    outputStr =  f'''
                    <td style="border-radius: 4px;
                               text-align: center;
                               width: {100 / size}%;
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

def getTableHTML(title, columnNames, dataRows):
     
    outputStr = f'''
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
                   '''
    
    for col in columnNames:
        outputStr += f' {getCellHTML(text=col, size=len(columnNames))} \n'

    outputStr += f'''
                             </tr>
                            
                             {dataRows}

                        </table>
                  '''     
    
    return outputStr

def getPropsHTML(team):
    numBooks = 3
    outputStr = ''

    for player in team:
            curPlayer = team[player]

            for propType in curPlayer:
                curPropType = curPlayer[propType]

                outputStr += '<tr> \n'
                outputStr += getCellHTML(player, 5)
                outputStr += getCellHTML(propType, 5)

                for book in ['Play Now', 'Pinnacle', 'Sports Interaction']:
                    playerOdds = ['']
                    if book in curPropType:
                        playerOdds = []
                        curProp = curPropType[book]
                        for amount, odd in curProp.odds:
                            overUnder = 'Over ' if amount[0] == 'O' else 'Under '
                            amount = overUnder + amount[1:]
                            playerOdds.append(f'{amount}: {odd}')

                    outputStr += getCellHTML(playerOdds, 5)
    return outputStr
    


                            

    