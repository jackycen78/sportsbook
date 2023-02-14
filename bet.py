from dataparser import *
from teamNames import teams, cities

class Bet:

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


class PlayNowBet(Bet):

    def __init__(self, data):
        super().__init__()
        self.book['name'] = 'Play Now'
        self.teams, self.spread, self.moneyLine, self.overUnder = PlayNowParser(data)


class SportsInteractionBet(Bet):

    def __init__(self, data):
        super().__init__()
        self.book['name'] = 'Sports Interaction'
        self.teams, self.spread, self.moneyLine, self.overUnder = SportsInteractionParser(data)



class Bet365Bet(Bet):

    def __init__(self, data):
        super().__init__()
        self.book['name'] = 'Bet 365'
        self.teams, self.spread, self.moneyLine, self.overUnder = Bet365Parser(data)






    
    