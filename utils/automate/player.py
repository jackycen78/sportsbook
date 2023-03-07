from models.playerprop import PlayerProp
from models.allplayerprops import AllPlayerProps
from utils.website import Website
from utils.helper import write_tests, clear_tests

import time

class PlayerProps():
    siteURL = ''
    propTypes = ['Points', 'Assists', 'Rebounds', '3 Pts Made', 'Points + Reb + Ass']
    propClass = ''
    book = ''
    gameInfo = ''
    bookFile = ''

    def __init__(self, site):
        self.site = site
        self.playerProps = []

    def go_to_site(self, sleepTime=4):
        self.site.go_to(self.siteURL, sleepTime)

    def add_player_props(self, parent=None):
        site = self.site

        gameInfo = site.find_class(self.gameInfoClass, parent)[0]
        props = site.find_class(self.propClass, parent)
        for prop in props:
            try:
                if prop:
                    playerProp = PlayerProp(self.book, gameInfo.text, prop.text)
                    if playerProp.is_valid():
                        self.playerProps.append(playerProp)

                        write_tests(self.bookFile, gameInfo.text, 'gameinfo')
                        write_tests(self.bookFile, prop.text, 'prop')
            except:
                pass

    def get_player_props(self):

        return self.playerProps

class PlayNow(PlayerProps):

    book = 'Play Now'
    bookFile = 'playnow'
    siteURL = 'https://www.playnow.com/sports/sport/9/basketball/matches?preselectedFilters=49'
    showMoreClass = 'content-loader__load-more-link'
    gameClass = 'event-list__item__event-market__market-count__link'
    propClass = 'event-panel--market---'
    todayClass = 'heading--timeband--today'
    tmrClass = 'heading--timeband--tomorrow'
    gameInfoClass = 'scoreboard--teams'
    allBetsClass = 'event-markets--basketball'
    hiddenPropsClass = 'collapsed'

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
        time.sleep(1)
        site.click_by_name('Player Props')
        time.sleep(1)


    def show_all_data(self):
        site = self.site

        allBets = site.find_class(self.allBetsClass)[0]
        hiddenProps = site.find_class(self.hiddenPropsClass, allBets)

        for prop in hiddenProps:
            if prop:
                prop.click()


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
    bookFile = 'pinnacle'
    siteURL = 'https://www.pinnacle.com/en/basketball/nba/matchups#period:0'
    gameClass = 'style_metadata__1FIzs'
    propClass = 'style_marketGroup__1-qlF'
    gameInfoClass = 'style_content__1q8Kz'

    def __init__(self, site):
        super().__init__(site)

    def automate(self):
        site = self.site
    
        self.go_to_site()
        numGames = len(site.find_class(self.gameClass))

        for i in range(numGames):
            self.go_to_game(i)
            self.add_player_props()
            self.go_to_site()

    def go_to_game(self, index):
        site = self.site

        game = site.find_class(self.gameClass)[index]
        game.click()
        site.click_by_name('Player Props')

class SportsInteraction(PlayerProps):
    
    book = 'Sports Interaction'
    bookFile = 'sportsinteraction'
    siteURL = 'https://www.sportsinteraction.com/basketball/nba-prop-betting/'
    gameClass = 'Game--listPage'
    gameInfoClass = 'GameHeader'
    propClass = 'BetType--displayAllEvents'

    def __init__(self, site):
        super().__init__(site)

    def automate(self):
        site = self.site
        self.go_to_site()

        allGames = site.find_class(self.gameClass)
        numGames = len(allGames)

        for i in range(numGames):
            curGame = site.find_class(self.gameClass)[i]
            self.add_player_props(parent=curGame)

def get_game_props():

    site = Website()
    allPlayerProps = AllPlayerProps()

    books = [PlayNow(site), 
             Pinnacle(site), 
             SportsInteraction(site),
             ]

    for book in books:
        clear_tests(book.bookFile)
        book.automate()
        props = book.get_player_props()
        allPlayerProps.add_prop(props)
    
    return allPlayerProps

