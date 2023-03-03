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

 
    
    