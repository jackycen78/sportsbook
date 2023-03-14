from models.playerprop import PlayerProp
from models.allplayerprops import AllPlayerProps
from utils.website import Website
from utils.config import PLAYER_BOOKS, WRITE_TESTS, MINUTES_BEFORE
from utils.helper import write_file, clear_tests, within_time

import time

class PlayerProps():
    siteURL = ''
    propTypes = ['Points', 'Assists', 'Rebounds', '3 Pts Made', 'Points + Reb + Ass']
    propClass = ''
    book = ''
    gameInfo = ''
    bookFile = ''
    minutesBefore = MINUTES_BEFORE

    def __init__(self, site):
        self.site = site
        self.playerProps = []

    def go_to_site(self, sleepTime=0.5):
        self.site.go_to(self.siteURL, sleepTime)

    def add_player_props(self, parent=None):
        site = self.site

        gameInfo = site.find_class(self.gameInfoClass, parent)[0]
        props = site.find_class(self.propClass, parent)

        for prop in props:
                if gameInfo and prop:
                    playerProp = PlayerProp(self.book, gameInfo.text, prop.text)
                    if playerProp.is_valid():
                        self.playerProps.append(playerProp)
                        
                        if WRITE_TESTS:
                            self.write_tests(text=f'{gameInfo.text}\n \n', 
                                            type='gameinfo')
                            
                            self.write_tests(text=f'{prop.text} \n \n', 
                                            type='prop')
                            
    def print_data(self, parent=None):
            site = self.site

            gameInfo = site.find_class(self.gameInfoClass, parent)[0]
            props = site.find_class(self.propClass, parent)

            for prop in props:
                    if gameInfo and prop:
                        playerProp = PlayerProp(self.book, gameInfo.text, prop.text)
                        print(playerProp)
                
    def write_tests(self, text, type):
        path = f'tests/props/{self.bookFile}/{type}.txt'
        write_file(path, text)

    def get_all_props(self):
        allProps = AllPlayerProps()

        for b in PLAYER_BOOKS:
            start_time = time.time()
            print(f'Getting {b} Player Props...')
            book = self.get_book_class(b)
            if WRITE_TESTS:
                clear_tests(book.bookFile)
            book.automate()
            allProps.add_prop(book.playerProps)
            print(f'{b} done in {round(time.time() - start_time, 2)} seconds')

        return allProps

    def get_book_class(self, book):
        books = {'Play Now': PlayNow(self.site),
                 'Pinnacle': Pinnacle(self.site),
                 'Sports Interact': SportsInteract(self.site),
                 }
        return books[book]

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
    timeClass = 'event-list__item__event-market-footer'

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
            if self.valid_time(i):
                self.go_to_game(i)
                self.show_all_data()
                self.add_player_props()
                self.go_to_site()
    
    def valid_time(self, i):
        todayBets = self.site.find_class(self.todayClass)[0]
        timeInfo = self.site.find_class(self.timeClass, todayBets)[i].text

        if 'Today' in timeInfo:
            return False
        timeText = timeInfo.split('\n')[0]

        timeAway = 0
        for t in timeText.split(' '):
            if t[-1] == 'h':
                timeAway += int(t[:-1]) * 60
            if t[-1] == 'm':
                timeAway += int(t[:-1])

        if timeAway > self.minutesBefore:
            return False
        return True

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

    def print_data(self, parent=None):
        site = self.site

        gameInfo = site.find_class(self.gameInfoClass, parent)[0]
        props = site.find_class(self.propClass, parent)

        for prop in props:
                if gameInfo and prop:
                    playerProp = PlayerProp(self.book, gameInfo.text, prop.text)
                    print(playerProp)

class Pinnacle(PlayerProps):

    book = 'Pinnacle'
    bookFile = 'pinnacle'
    siteURL = 'https://www.pinnacle.com/en/basketball/nba/matchups#period:0'
    gameClass = 'style_metadata__1FIzs'
    propClass = 'style_marketGroup__1-qlF'
    gameInfoClass = 'style_content__1q8Kz'
    timeClass = 'style_matchupDate__1gnX6'

    def __init__(self, site):
        super().__init__(site)

    def automate(self):
        site = self.site
    
        self.go_to_site(2)
        numGames = len(site.find_class(self.gameClass))

        for i in range(numGames):
            if self.valid_time(i):
                self.go_to_game(i)
                self.add_player_props()
                self.go_to_site()

    def valid_time(self, i):
        timeInfo = self.site.find_class(self.timeClass)[i].text
        if timeInfo == 'Live Now':
            return False
        
        return within_time(gameTime=timeInfo, 
                           minutesBefore=self.minutesBefore)

    def go_to_game(self, index):
        site = self.site

        game = site.find_class(self.gameClass)[index]
        game.click()
        site.click_by_name('Player Props')

class SportsInteract(PlayerProps):
    
    book = 'Sports Interact'
    bookFile = 'sportsinteract'
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
            if self.valid_time(i):
                curGame = site.find_class(self.gameClass)[i]
                self.add_player_props(parent=curGame)

    def valid_time(self, i):
        timeInfo = self.site.find_class(self.gameClass)[i].text
        timeInfo = timeInfo.split('\n')[0]
        
        return within_time(gameTime=timeInfo, 
                           minutesBefore=self.minutesBefore,
                           hoursAhead=3)