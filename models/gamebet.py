from utils.parser.game import PlayNow, Pinnacle, Bet365, SportsInteraction
from utils.names.game import getCityName, getTeamName
from utils.helper import decimalToAmerican


class GameBet:

    def __init__(self, book, data):
        self.book = book
        self.parser = self.get_parser()
        self.teams, self.spread, self.moneyLine, self.overUnder = self.parser.parse_game(data)
    
    def get_parser(self):
        books = {'Play Now': PlayNow(),
                 'Pinnacle': Pinnacle(),
                 'Sports Interaction': SportsInteraction(),
                 'Bet 365': Bet365(),
                 }
        return books[self.book]
    
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
        return getCityName(self.teams["home"])

    def get_away_city(self):
        return getCityName(self.teams["away"])

    def get_home_team(self):
        return getTeamName(self.teams["home"])

    def get_away_team(self):
        return getTeamName(self.teams["away"])

    def get_teams(self):
        return f'{self.teams["away"]} at {self.teams["home"]}'

    def get_book(self):
        return self.books

    def __str__(self) -> str:
        return \
               f'''Book: {self.book} \n 
                   Home Team: {self.teams["home"]}\n 
                   Away Team: {self.teams["away"]} \n
                '''