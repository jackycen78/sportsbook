
def playNowPlayerProps(site):

    playNowURL = 'https://www.playnow.com/sports/sport/9/basketball/matches?preselectedFilters=49'
    showMoreClass = 'content-loader__load-more-link'
    gameClass = 'event-list__item__event-market__market-count__link'
    betClass = 'event-panel--market---'
    todayClass = 'heading--timeband--today'
    
    site.go_to(playNowURL, sleepTime=2)
    site.click_by_class(showMoreClass, sleepTime=2)

    todayBets = site.find_class(todayClass)[0]
    numGames = len(site.find_class(gameClass, todayBets))
    playerProps = []

    for i in range(numGames):
        todayBets = site.find_class(todayClass)[0]
        game = site.find_class(gameClass, todayBets)[i]
        game.click()

        site.click_by_name('Player Props')
        bets = site.find_class(betClass)
        for bet in bets:
            try:
                playerProps.append(bet.text)
            except:
                pass

        site.go_to(playNowURL, sleepTime=2)
        site.click_by_class(showMoreClass, sleepTime=2)
    print(playerProps)



def bet365PlayerProps(site):

    allGamesURL = 'https://www.bet365.com/#/AC/B18/C20604387/D48/E1453/F10/'
    gameClass = 'scb-ParticipantFixtureDetailsHigherBasketball_LhsContainer'

    site.go_to(allGamesURL)
    games = site.find_class(gameClass)
    numGames = len(games)

    propTypes = ['Player Points',
                 'Player Assists',
                 'Player Rebounds',
                 'Player Steals',
                 'Player Blocks',
                 ]
    playerProps = []
    

    for i in range(numGames):
        games = site.find_class(gameClass)
        games[i].click()

        site.refresh_page()
        site.click_by_name('Player Props')

        for prop in propTypes:
            curProp = site.find_name(name=prop,
                                     exact=True)[0]
            curProp.click()
            #site.click_by_name(name='Show more', 
            #                   parent=curProp)

            bet = site.find_name(name=prop, 
                                 path='/ancestor::*/following-sibling::div',
                                 exact=True)[0].text
            
            playerProps.append(prop + bet)
            print(prop + bet)

        site.go_to(allGamesURL)
    print(playerProps)



def pinnaclePlayerProps(site):

    allGamesURL = 'https://www.pinnacle.com/en/basketball/nba/matchups#period:0'
    gameClass = 'style_metadata__1FIzs'
    betClass = 'style_marketGroup__1-qlF'

    site.go_to(allGamesURL)
    numGames = len(site.find_class(gameClass))
    playerProps = []

    print(numGames)
    for i in range(numGames):
        print(i)
        game = site.find_class(gameClass)[i]
        game.click()

        site.click_by_name('Player Props')
        bets = site.find_class(betClass)
        for bet in bets:
            playerProps.append(bet.text)
        site.go_to(allGamesURL)
    
    print(playerProps)

