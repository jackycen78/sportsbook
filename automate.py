from bet import * 
import time

def getPlayNowBets(site):

    playNowURL = 'https://www.playnow.com/sports/sport/9/basketball/matches?preselectedFilters=49'
    showmore = '//*[@id="sports-wrapper"]/div/div/div/div/main/section/div[2]/div[2]/div/div/div[2]/div/article/div/div/div[1]/article/div[2]/div/div[2]/div/div[2]/div/a'
    table = '/html/body/section/section/div[2]/div/div/div/div/main/section/div[2]/div[2]/div/div/div[2]/div/article/div/div/div[1]/article/div[2]/div/div[2]'

    site.go_to(playNowURL)
    time.sleep(2)
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

    return betsList

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

    return betsList


def getBet365Bets(site):

    bet365URL = 'https://www.bet365.com/#/AC/B18/C20604387/D48/E1453/F10/'
    table = '/html/body/div[1]/div/div[4]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]'
    teamsLoc = '/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]'
    spreadLoc = '/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]'
    overunderLoc = '/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]'
    moneylineLoc = '/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[4]'


    site.go_to(bet365URL)
    time.sleep(1)

    teams = site.locate(teamsLoc).text.split('\n')[2:]
    spreads = site.locate(spreadLoc).text.split('\n')[1:]
    overUnders = site.locate(overunderLoc).text.split('\n')[1:]
    moneyLines = site.locate(moneylineLoc).text.split('\n')[1:]
    numBets = len(teams) // 3

 
    betsList = []
    
    for i in range(numBets):
        betsList.append(Bet365Bet([teams[i * 3: i * 3 + 3], 
                                   spreads[i * 4: i * 4 + 4], 
                                   overUnders[i * 4: i * 4 + 4], 
                                   moneyLines[i * 2: i * 2 + 2],
                                ]))

    return betsList

