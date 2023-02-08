from parser import *

class Bet:

    def __init__(self):
        self.homeTeam = {'name': None,
                         'spread' : None,
                         'spreadOdds' : None,
                         'moneyline': None,
                        }
        self.awayTeam = {'name': None,
                         'spread' : None,
                         'spreadOdds' : None,
                         'moneyline': None,
                        }
        self.overUnder = {'over': None,
                          'overOdds': None,
                          'under': None,
                          'underOdds': None,
                          }
        self.time = None

    def __str__(self) -> str:
        return f'Home Team: {self.homeTeam["name"]} \n \
                    Money Line: {self.homeTeam["moneyline"]} \n \
                 Away Team: {self.awayTeam["name"]} \n \
                    Money Line: {self.awayTeam["moneyline"]} \n '


class PlayNowBet(Bet):

    def __init__(self, data):
        super().__init__()
        self.homeTeam, self.awayTeam, self.overUnder = PlayNowParser(data)




    
    