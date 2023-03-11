from utils.parser.player import PlayNowPlayerParser, PinnaclePlayerParser, SportsInteractParser

class PlayerProp:

    def __init__(self, book, gameInfo, bet):
        self.book = book
        self.parser = self.get_parser()
        self.player, self.type, self.odds = self.parser.parse_prop(bet)
        self.time, self.home, self.away = self.parser.parse_game_info(gameInfo)

    def get_parser(self):
        books = {'Play Now': PlayNowPlayerParser(),
                 'Pinnacle': PinnaclePlayerParser(),
                 'Sports Interact': SportsInteractParser(),
                 }
        
        return books[self.book]
    
    def is_valid(self):
        return self.player and self.type and self.odds

    def __str__(self):
        output = ''
        output += f'{self.away} at {self.home} {self.time} \n'
        output += f'{self.book} \n'
        output +=  f'{self.player}: {self.type} \n'
        for amount, odd in self.odds:
            overUnder = 'Over' if amount[0] == 'O' else 'Under'
            amount = overUnder + amount[1:]
            output += f'    {amount}: {odd} \n'
        return output
    