from bet import * 
import time

def getPlayNowBets(site):

    playNowURL = 'https://www.playnow.com/sports/sport/9/basketball/matches?preselectedFilters=49'
    showMoreClass = 'content-loader__load-more-link'
    
    todayClass = 'heading--timeband--today'
    nextToGoClass = 'heading--timeband--next_to_go'
    liveClass = 'heading--timeband--live'
    tmrClass = 'heading--timeband--tomorrow'

    nbaClass = 'event-list__item--basketball'
    teamClass = 'event-card__body__name'
    spreadClass = 'market__body--WH'
    moneyLineClass = 'market__body--HH'
    overUnderClass = 'market__body--HL'

    site.go_to(playNowURL, sleepTime=2)
    site.click_by_class(showMoreClass, sleepTime=1)


    bets = site.find_class(childClassName=nbaClass,
                           parent=site.find_class(tmrClass)[0])
    #bets = site.find_child_by_class(site.class_locate(todayClass)[0], nbaClass)
    #bets += site.find_child_by_class(site.class_locate(liveClass)[0], nbaClass)
    betsList = []

    for bet in bets:
        teams = site.find_class(teamClass, bet)[0]
        spreads = site.find_class(spreadClass, bet)[0]
        moneyLines = site.find_class(moneyLineClass, bet)[0]
        overUnders = site.find_class(overUnderClass, bet)[0]
        betsList.append(PlayNowParser([teams, 
                                       spreads, 
                                       moneyLines, 
                                       overUnders]))
    return betsList

def getSportsInteractionBets(site):

    sportsInteractionURL = 'https://www.sportsinteraction.com/basketball/nba-betting-lines/'
    nbaClass = 'Game--mainMarkets'
    todayClass = 'GameDateGroup'
    teamClass = 'GameHeader__name'
    betTypesClass = 'MainMarketTable__event'

    site.go_to(sportsInteractionURL, sleepTime=2)

    todayBets = site.find_class(todayClass)[0]
    bets = site.find_class(nbaClass, todayBets)
    betsList = []

    for bet in bets:
        teams = site.find_class(teamClass, bet) 
        spreads, moneylines, overUnders = site.find_class(betTypesClass, bet)[:3]
        betsList.append(SportsInteractionParser([teams[0], 
                                                spreads, 
                                                moneylines, 
                                                overUnders]))
    return betsList


def getBet365Bets(site):

    bet365URL = 'https://www.bet365.com/#/AC/B18/C20604387/D48/E1453/F10/'
    teamsLoc = '/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]'
    spreadLoc = '/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]'
    overunderLoc = '/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]'
    moneylineLoc = '/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[4]'


    site.go_to(bet365URL, sleepTime=1)
    
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

