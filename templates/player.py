from templates.tables import getCellHTML, getTableHTML
from utils.config import PLAYER_PROPS, PLAYER_BOOKS

def getPropsHTML(team):
    numBooks = len(PLAYER_BOOKS)
    outputStr = ''

    for player in team:
            curPlayer = team[player]

            for propType in curPlayer:
                curPropType = curPlayer[propType]

                outputStr += '<tr> \n'
                outputStr += getCellHTML(player, numBooks + 2)
                outputStr += getCellHTML(propType, numBooks + 2)

                for book in PLAYER_BOOKS:
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
    


                            

    