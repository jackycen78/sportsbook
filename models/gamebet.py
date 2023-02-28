from utils.parser.game import *
from utils.teamnames import teams, cities
from utils.helper import decimalToAmerican

class GameBet:

    def __init__(self):
        self.time = None
        self.book = {'name': None}
        self.teams = {'home': None,
                      'away': None,                      
                     }

        self.spread = {'homeSpread' : None,
                       'homeSpreadOdds' : None,
                       'awaySpread' : None,
                       'awaySpreadOdds' : None,
                       }

        self.moneyLine = {'homeMoneyLine' : None,
                          'awayMoneyLine' : None,
                          }

        self.overUnder = {'over': None,
                          'overOdds': None,
                          'under': None,
                          'underOdds': None,
                          }
        
        self.odds = [('spread', 'homeSpreadOdds'), 
                     ('spread', 'awaySpreadOdds'),
                     ('moneyLine', 'homeMoneyLine'),
                     ('moneyLine', 'awayMoneyLine'),
                     ('overUnder', 'overOdds'),
                     ('overUnder', 'underOdds'), 
                     ]

    def changeToAmerican(self):
        self.spread['homeSpreadOdds'] = decimalToAmerican(self.spread['homeSpreadOdds'])
        self.spread['awaySpreadOdds'] = decimalToAmerican(self.spread['awaySpreadOdds'])
        self.moneyLine['homeMoneyLine'] = decimalToAmerican(self.moneyLine['homeMoneyLine'])
        self.moneyLine['awayMoneyLine'] = decimalToAmerican(self.moneyLine['awayMoneyLine'])
        self.overUnder['overOdds'] = decimalToAmerican(self.overUnder['overOdds'])
        self.overUnder['underOdds'] = decimalToAmerican(self.overUnder['underOdds'])

    def get_spread(self):
        return self.spread

    def get_cities(self):
        return f'{self.get_away_city()} at {self.get_home_city()}'   

    def get_home_city(self):
        return cities[self.teams["home"]]

    def get_away_city(self):
        return cities[self.teams["away"]]

    def get_home_team(self):
        return teams[self.teams["home"]]

    def get_away_team(self):
        return teams[self.teams["away"]]

    def get_teams(self):
        return f'{self.teams["away"]} at {self.teams["home"]}'

    def get_book(self):
        return self.books

    def __str__(self) -> str:
        return \
               f'''Book: {self.book["name"]} \n 
                   Home Team: {self.teams["home"]}\n 
                   Away Team: {self.teams["away"]} \n
                '''
                
class PlayNowGameBet(GameBet):

    def __init__(self, data):
        super().__init__()
        self.book['name'] = 'Play Now'
        self.teams, self.spread, self.moneyLine, self.overUnder = PlayNowParser(data)

class SportsInteractionGameBet(GameBet):

    def __init__(self, data):
        super().__init__()
        self.book['name'] = 'Sports Interaction'
        self.teams, self.spread, self.moneyLine, self.overUnder = SportsInteractionParser(data)

class Bet365GameBet(GameBet):

    def __init__(self, data):
        super().__init__()
        self.book['name'] = 'Bet 365'
        self.teams, self.spread, self.moneyLine, self.overUnder = Bet365Parser(data)


class PinnacleGameBet(GameBet):

    def __init__(self, data):
        super().__init__()
        self.book['name'] = 'Pinnacle'
        self.teams, self.spread, self.moneyLine, self.overUnder = PinnacleParser(data)





    
    