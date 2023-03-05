from utils.parser.player import PlayNowPlayerParser, PinnaclePlayerParser

class PlayerProp:

    def __init__(self, book, bet):
        self.book = book
        self.parser = self.get_parser()
        self.player, self.type, self.odds = self.parser.parseProp(bet)

    def get_parser(self):
        books = {'Play Now': PlayNowPlayerParser(),
                 'Pinnacle': PinnaclePlayerParser(),
                 }
        
        return books[self.book]
    
    def is_valid(self):
        return self.player and self.type and self.odds

    def __str__(self):
        output =  f'{self.player}: {self.type} \n'
        for amount, odd in self.odds:
            overUnder = 'Over ' if amount[0] == 'O' else 'Under '
            amount = overUnder + amount[1:]

            output += f'    {amount}: {odd} \n'
        return output
    