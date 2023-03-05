from models.playerprop import PlayerProp
import time

class PlayerProps():
    siteURL = ''
    propTypes = ['Points', 'Assists', 'Rebounds', '3 Pts Made', 'Points + Reb + Ass']
    betClass = ''
    book = ''

    def __init__(self, site):
        self.site = site
        self.playerProps = []

    def go_to_site(self, sleepTime=3):
        self.site.go_to(self.siteURL, sleepTime)

    def add_player_props(self):
        site = self.site

        bets = site.find_class(self.betClass)
        for bet in bets:
            if bet:
                playerProp = PlayerProp(self.book, bet.text)
                if playerProp.is_valid():
                    self.playerProps.append(playerProp)
                    print(playerProp)

    def get_player_props(self):

        return self.playerProps

class PlayNow(PlayerProps):

    book = 'Play Now'
    siteURL = 'https://www.playnow.com/sports/sport/9/basketball/matches?preselectedFilters=49'
    showMoreClass = 'content-loader__load-more-link'
    gameClass = 'event-list__item__event-market__market-count__link'
    betClass = 'event-panel--market---'
    todayClass = 'heading--timeband--today'
    allBetsClass = 'event-markets--basketball'
    hiddenBetsClass = 'collapsed'

    def __init__(self, site):
        super().__init__(site)

    def go_to_site(self):
        site = self.site
        site.go_to(self.siteURL, sleepTime=2)
        site.click_by_class(self.showMoreClass, sleepTime=2)
    
    def automate(self):
        site = self.site
        self.go_to_site()

        todayBets = site.find_class(self.todayClass)[0]
        numGames = len(site.find_class(self.gameClass, todayBets))

        for i in range(numGames):
            self.go_to_game(i)
            self.show_all_data()
            self.add_player_props()
            self.go_to_site()
    
    def go_to_game(self, index):
        site = self.site

        todayBets = site.find_class(self.todayClass)[0]
        game = site.find_class(self.gameClass, todayBets)[index]
        game.click()
        site.click_by_name('Player Props')
        time.sleep(2)


    def show_all_data(self):
        site = self.site

        allBets = site.find_class(self.allBetsClass)[0]
        hiddenBets = site.find_class(self.hiddenBetsClass, allBets)

        for bet in hiddenBets:
            if bet:
                bet.click()


class Bet365(PlayerProps):
    
    siteURL = 'https://www.bet365.com/#/AC/B18/C20604387/D48/E1453/F10/'
    gameClass = 'scb-ParticipantFixtureDetailsHigherBasketball_LhsContainer'

    def __init__(self, site):
        super().__init__(site)


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

class Pinnacle(PlayerProps):

    book = 'Pinnacle'
    siteURL = 'https://www.pinnacle.com/en/basketball/nba/matchups#period:0'
    gameClass = 'style_metadata__1FIzs'
    betClass = 'style_marketGroup__1-qlF'

    def __init__(self, site):
        super().__init__(site)

    def automate(self):
        site = self.site
    
        self.go_to_site()
        numGames = len(site.find_class(self.gameClass))

        for i in range(numGames):
            print(i, numGames)
            self.go_to_game(i)
            self.add_player_props()
            self.go_to_site()

    def go_to_game(self, index):
        site = self.site

        game = site.find_class(self.gameClass)[index]
        game.click()
        site.click_by_name('Player Props')



