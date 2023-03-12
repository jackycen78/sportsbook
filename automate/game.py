from models.gamebet import GameBet
from models.allgamebets import AllBets
from utils.website import Website
from utils.config import GAME_BOOKS, PLAYNOW_TIMES
from utils.helper import write_file, clear_file


class GameBets():

    def __init__(self, site):
        self.site = site
        self.bets = []

    def go_to_site(self, sleepTime=2):
        self.site.go_to(self.siteURL, sleepTime)

    def automate(self):
        self.go_to_site()
        betList = self.find_bets()
        self.clear_tests()
        for bet in betList:
            self.add_game_data(bet)

    def create_bet(self, data):
        self.write_tests(data)
        return GameBet(self.book, data)
    
    def write_tests(self, data):
        path = f'tests/games/{self.bookFile}/game.txt'
        for d in data:
            write_file(path, f'{d}\n\n')

    def clear_tests(self):
        path = f'tests/games/{self.bookFile}/game.txt'
        clear_file(path)

    def check_game_data(self, data):
        for i, d in enumerate(data):
            if d:
                data[i] = d.text
            else:
                data[i] = ''
        return data

    def get_all_bets(self):
        allBets = AllBets()

        for b in GAME_BOOKS:
            book = self.get_book_class(b)
            book.automate()
            allBets.add_bets(book.bets)

        return allBets
    
    def get_book_class(self, book):
        books = {'Play Now': PlayNow(self.site),
                 'Pinnacle': Pinnacle(self.site),
                 'Sports Interact': SportsInteract(self.site),
                 }
        return books[book]

class PlayNow(GameBets):

    book = 'Play Now'
    bookFile = 'playnow'
    siteURL = 'https://www.playnow.com/sports/sport/9/basketball/matches?preselectedFilters=49'
    showMoreClass = 'content-loader__load-more-link'
    
    timeClasses = {'today' : 'heading--timeband--today',
                   'next' : 'heading--timeband--next_to_go',
                   'live' : 'heading--timeband--live',
                   'tommorrow' : 'heading--timeband--tomorrow',
                   }

    nbaClass = 'event-list__item--basketball'
    teamClass = 'event-card__body__name'
    spreadClass = 'market__body--WH'
    moneyLineClass = 'market__body--HH'
    overUnderClass = 'market__body--HL'
    
    def __init__(self, site):
        super().__init__(site)

    def go_to_site(self, sleepTime=2):
        super().go_to_site(sleepTime)
        self.site.click_by_class(self.showMoreClass, sleepTime=1)

    def find_bets(self):
        site = self.site
        bets = []

        for time in PLAYNOW_TIMES:
            timeClass = self.timeClasses[time]

            if site.class_exists(timeClass):
                bets += site.find_class(className=self.nbaClass,
                                        parent=site.find_class(timeClass)[0])
        return bets
                
    def add_game_data(self, bet):
        site = self. site

        teams = site.find_class(self.teamClass, bet)[0]
        spreads = site.find_class(self.spreadClass, bet)[0]
        moneyLines = site.find_class(self.moneyLineClass, bet)[0]
        overUnders = site.find_class(self.overUnderClass, bet)[0]

        data = self.check_game_data([teams, 
                                     spreads, 
                                     moneyLines, 
                                     overUnders])

        newBet = self.create_bet(data)

        newBet.changeToAmerican()
        self.bets.append(newBet)

class SportsInteract(GameBets):

    book = 'Sports Interact'
    bookFile = 'sportsinteract'
    siteURL = 'https://www.sportsinteraction.com/basketball/nba-betting-lines/'
    
    nbaClass = 'Game--mainMarkets'
    todayClass = 'GameDateGroup'
    teamClass = 'GameHeader__name'
    betTypesClass = 'MainMarketTable__event'
    
    def __init__(self, site):
        super().__init__(site)

    def find_bets(self):
        site = self.site

        todayBets = site.find_class(self.todayClass)[0]
        return site.find_class(self.nbaClass, todayBets)

    def add_game_data(self, bet):
            site = self.site

            teams = site.find_class(self.teamClass, bet)[0]

            spreads, moneyLines, overUnders = site.find_class(self.betTypesClass, bet)[:3]
            data = self.check_game_data([teams, 
                                         spreads, 
                                         moneyLines, 
                                         overUnders])
            
            newBet = self.create_bet(data)
            newBet.changeToAmerican()

            self.bets.append(newBet)

def getBet365GameBets(site):

    bet365URL = 'https://www.bet365.com/#/AC/B18/C20604387/D48/E1453/F10/'
    betTypesClass = 'gl-Participant_General'
    teamsClass = 'scb-ParticipantFixtureDetailsHigherBasketball_TeamNames'

    site.go_to(bet365URL)
    site.refresh_page()
    site.refresh_page()
    betsList = []

    teams = site.find_class(teamsClass)
    numTeams = len(teams)
    betTypes = site.find_class(betTypesClass)

    spreads = betTypes[:numTeams * 2]
    overUnders = betTypes[numTeams * 2: numTeams * 4]
    moneyLines = betTypes[numTeams * 4:]
    
    for i in range(numTeams):
        betsList.append(GameBet('Bet 365', [teams[i], 
                                 spreads[i * 2: (i + 1) * 2], 
                                 moneyLines[i * 2: (i + 1) * 2], 
                                 overUnders[i * 2: (i + 1) * 2], 
                                ]))
    return betsList

class Pinnacle(GameBets):

    book = 'Pinnacle'
    bookFile = 'pinnacle'
    siteURL = 'https://www.pinnacle.com/en/basketball/nba/matchups#period:0'

    betsClass = 'style_row__3q4g_'
    teamClass = 'style_matchupMetadata__Ey_nj'
    betTypesClass = 'style_buttons__XEQem'

    def __init__(self, site):
        super().__init__(site)

    def find_bets(self):
        site = self.site
        return site.find_class(self.betsClass)[1:]

    def add_game_data(self, bet):
            site = self.site
            teams = site.find_class(self.teamClass, bet)[0]
            spreads, moneyLines, overUnders = site.find_class(self.betTypesClass, bet)[:3]
            data = self.check_game_data([teams, 
                                         spreads, 
                                         moneyLines, 
                                         overUnders])
            
            newBet = self.create_bet(data)
            newBet.changeToAmerican()
            self.bets.append(newBet)
