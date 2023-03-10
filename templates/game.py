from templates.tables import getCellHTML, getTableHTML
from utils.config import GAME_BETS, GAME_SITES
from templates.email import getEmailHTML

def createGameEmail(games):
    columns = ['Game'] + GAME_SITES
    content = []
    for betType in GAME_BETS:
        contentHTML = getTableHTML(title=betType, 
                                   columnNames=columns,
                                   dataRows=createGameRows(games, betType)
                     )
        content.append(contentHTML)
    return getEmailHTML(content)


def createGameRows(games, betType):
    numBooks = len(GAME_SITES)
    format = getFormat(betType)
    outputStr = ''
    for team in games:
        if len(games[team]) == numBooks:
            outputStr += '<tr> \n'
            curGame = games[team][0]
            outputStr += getCellHTML(text=[curGame.get_away_city(), 
                                           'at', 
                                           curGame.get_home_city(),
                                           ],
                                     size=numBooks+1)
            for bet in games[team]:
                outputStr+= getCellHTML(format(bet), size=numBooks+1)
            outputStr += '</tr>'
    return outputStr

def getFormat(betType):
    if betType == 'Money Lines':
        return moneyLineFormat
    if betType == 'Spreads':
        return spreadFormat
    if betType == 'Over Unders':
        return overUnderFormat

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
    over = f"O {bet.overUnder['over']}" if bet.overUnder['over'] else ''
    overOdds = bet.overUnder['overOdds']
    under = f"O {bet.overUnder['under']}" if bet.overUnder['under'] else ''
    underOdds = bet.overUnder['underOdds']

    format = [over,
              overOdds,
              under,
              underOdds,
              ]
    return format