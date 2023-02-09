from bet import * 
import time

def getPlayNowBets(site):

    playNowURL = 'https://www.playnow.com/sports/sport/9/basketball/matches?preselectedFilters=49'
    showmore = '//*[@id="sports-wrapper"]/div/div/div/div/main/section/div[2]/div[2]/div/div/div[2]/div/article/div/div/div[1]/article/div[2]/div/div[2]/div/div[2]/div/a'
    table = '/html/body/section/section/div[2]/div/div/div/div/main/section/div[2]/div[2]/div/div/div[2]/div/article/div/div/div[1]/article/div[2]/div/div[2]'

    site.go_to(playNowURL)
    site.click(showmore)

    time.sleep(1)
    
    data = site.locate(table).text.split('\n')
    dataLength = 18
    # Remove header
    data = data[5:]

    betsList = []
    numBets = len(data) // dataLength

    
    for i in range(numBets):
        betsList.append(PlayNowBet(data[i * dataLength: (i + 1) * dataLength]))

    for bet in betsList:
        print(bet)

def getSportsInteractionBets(site):

    sportsInteractionURL = 'https://www.sportsinteraction.com/basketball/nba-betting-lines/'
    table = '/html/body/div[2]/div/div[4]/div[4]/div[2]/ul/li'

    site.go_to(sportsInteractionURL)
    time.sleep(1)

    data = site.locate(table).text.split('\n')
    dataLength = 17
    # Remove header
    data = data[1:]

    betsList = []
    numBets = len(data) // dataLength
    
    for i in range(numBets):
        betsList.append(SportsInteractionBet(data[i * dataLength: (i + 1) * dataLength]))

    for bet in betsList:
        print(bet)


def getBet365Bets(site):

    bet365URL = 'https://www.bet365.com/#/AC/B18/C20604387/D48/E1453/F10/'
    table = '/html/body/div[1]/div/div[4]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]'

    site.go_to(bet365URL)
    time.sleep(1)

    data = site.locate(table).text.split('\n')
    data = data[1:]

    spreadStart = data.index('Spread')
    spreadEnd = data.index('Spread', data.index('Spread') + 1)

    uOStart = data.index('Total')
    uOEnd = data.index('Total', data.index('Total') + 1)

    mLStart = data.index('Money Line')
    mLEnd = data.index('Money Line', data.index('Money Line') + 1)

    numBets = (spreadEnd + 1  - spreadStart) // 4

    teams = data[:numBets * 3]
    spreads = data[spreadStart + 1: spreadEnd]
    overUnders = data[uOStart + 1: uOEnd]
    moneyLines = data[mLStart + 1: mLEnd]

    betsList = []
    print(numBets)
    
    print(teams, spreads, overUnders, moneyLines)
    for i in range(numBets):
        betsList.append(Bet365Parser(teams[i * 2: i * 2 + 2], 
                                     spreads[i * 4: i * 4 + 4], 
                                     overUnders[i * 4: i * 4 + 4], 
                                     moneyLines[i * 2: i * 2 + 2],
                                    ))

    #for bet in betsList:
    #    print(bet)

