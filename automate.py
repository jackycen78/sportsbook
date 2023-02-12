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
                           parent=site.find_class(liveClass)[0])
    #bets = site.find_child_by_class(site.class_locate(todayClass)[0], nbaClass)
    #bets += site.find_child_by_class(site.class_locate(liveClass)[0], nbaClass)
    betsList = []

    for bet in bets:
        teams = site.find_class(teamClass, bet)[0]
        spreads = site.find_class(spreadClass, bet)[0]
        moneyLines = site.find_class(moneyLineClass, bet)[0]
        overUnders = site.find_class(overUnderClass, bet)[0]
        betsList.append(PlayNowBet([teams, 
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
        betsList.append(SportsInteractionBet([teams[0], 
                                                spreads, 
                                                moneylines, 
                                                overUnders]))
    return betsList


def getBet365Bets(site):

    bet365URL = 'https://www.bet365.com/#/AC/B18/C20604387/D48/E1453/F10/'

    betTypesClass = 'gl-Participant_General'
    teamsClass = 'scb-ParticipantFixtureDetailsHigherBasketball_TeamNames'

    site.go_to(bet365URL, sleepTime=1)
    betsList = []

    teams = site.find_class(teamsClass)
    numTeams = len(teams)
    betTypes = site.find_class(betTypesClass)

    spreads = betTypes[:numTeams * 2]
    overUnders = betTypes[numTeams * 2: numTeams * 4]
    moneyLines = betTypes[numTeams * 4:]
    
    for i in range(numTeams):
        betsList.append(Bet365Bet([teams[i], 
                                   spreads[i * 2: (i + 1) * 2], 
                                   moneyLines[i * 2: (i + 1) * 2], 
                                   overUnders[i * 2: (i + 1) * 2], 
                                ]))

    return betsList

