from templates.tables import getCellHTML, getTableHTML, getColumnHeadersHTML
from templates.email import getEmailHTML
from utils.config import PLAYER_PROPS, PLAYER_BOOKS

def createPlayerEmail(props):
    columns = ['Player', 'Prop'] + PLAYER_BOOKS

    content = []
    for team in props.games:
        curTeam = props.games[team]
        contentHTML = getTableHTML(title=team, 
                                   columns=getColumnHeadersHTML(columns),
                                   dataRows=createPlayerRows(curTeam))
        content.append(contentHTML)

    return getEmailHTML(content)

def createPlayerRows(team):
    numBooks = len(PLAYER_BOOKS)
    outputStr = ''

    for player in team:
            curPlayer = team[player]

            for i, propType in enumerate(curPlayer):
                
                curPropType = curPlayer[propType]
                outputStr += '<tr> \n'
                if i == 0:
                    outputStr += getCellHTML(player, numBooks + 2, len(curPlayer))

                outputStr += getCellHTML(propType, numBooks + 2)
                for book in PLAYER_BOOKS:
                    playerOdds = ['']

                    if book in curPropType:
                        playerOdds = []
                        curProp = curPropType[book]
                        for amount, odd in curProp.odds:
                            overUnder = 'Over ' if amount[0] == 'O' else 'Under '
                            amount = overUnder + amount[1:]
                            playerOdds.append(f'''<div style="float:left;width:49.35%;text-align:right">{amount}:</div> 
                                                  <div style="float:right;width:49.35%;text-align:left">{odd}</div> 
                                               '''
                                              )

                    outputStr += getCellHTML(playerOdds, numBooks + 2)
    return outputStr
    


                            

    