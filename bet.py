from dataparser import *

class Bet:

    def __init__(self):
        self.homeTeam = None
        self.awayTeam = None
        self.time = None
        self.book = None

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

    def to_dict(self):
        pass

    def __str__(self) -> str:
        return \
               f'Home Team: {self.homeTeam} \n \
                 Money Line: {self.moneyLine["homeMoneyLine"]} \n \
                 Spread: {self.spread["homeSpread"]}   \n \
                 Spread Odds: {self.spread["homeSpreadOdds"]}   \n \n \
                 Away Team: {self.awayTeam} \n \
                 Money Line: {self.moneyLine["awayMoneyLine"]} \n \
                 Spread: {self.spread["awaySpread"]}  \n \
                 Spread Odds: {self.spread["awaySpreadOdds"]}   \n \n \
                 Over {self.overUnder["over"]}: {self.overUnder["overOdds"]} \n \
                 Under {self.overUnder["under"]}: {self.overUnder["underOdds"]} \n \
                 '


class PlayNowBet(Bet):

    def __init__(self, data):
        super().__init__()
        self.book = 'Play Now'
        self.homeTeam, self.awayTeam, self.spread, self.moneyLine, self.overUnder = PlayNowParser(data)

class SportsInteractionBet(Bet):

    def __init__(self, data):
        super().__init__()
        self.book = 'Sports Interaction'
        self.homeTeam, self.awayTeam, self.spread, self.moneyLine, self.overUnder = SportsInteractionParser(data)


class Bet365Bet(Bet):

    def __init__(self, data):
        super().__init__()
        self.book = 'Bet 365'
        self.homeTeam, self.awayTeam, self.spread, self.moneyLine, self.overUnder = Bet365Parser(data)






    
    