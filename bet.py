from dataparser import *

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

    def get_moneyLine(self):
        return self.moneyLine

    def get_overUnder(self):
        return self.overUnder

    def get_teams(self):
        return {'Teams': f'{self.teams["away"]} at {self.teams["home"]}'}

    def get_book(self):
        return {'Sportsbook': self.book}

    def __str__(self) -> str:
        return \
               f'Book: {self.book["name"]} \n \
Home Team: {self.teams["home"]}\n \
Money Line: {self.moneyLine["homeMoneyLine"]} \n \
Spread: {self.spread["homeSpread"]}   \n \
Spread Odds: {self.spread["homeSpreadOdds"]}   \n \n \
Away Team: {self.teams["away"]} \n \
Money Line: {self.moneyLine["awayMoneyLine"]} \n \
Spread: {self.spread["awaySpread"]}  \n \
Spread Odds: {self.spread["awaySpreadOdds"]}   \n \n \
Over {self.overUnder["over"]}: {self.overUnder["overOdds"]} \n \
Under {self.overUnder["under"]}: {self.overUnder["underOdds"]} \n \
                 '


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






    
    