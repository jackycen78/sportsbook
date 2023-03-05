class AllPlayerProps:

    def __init__(self):
        self.games = {}

    def add_prop(self, props):

        for prop in props:
            if prop.player not in self.games:
                self.games[prop.player] = []
                
            self.games[prop.player].append(prop)

    def __str__(self):
        output = ''
        for player in self.games:
            output += f'{player} \n'

            for prop in self.games[player]:
                output += f'{prop.book}: {prop.type} \n'

                for amount, odd in prop.odds:
                    overUnder = 'Over ' if amount[0] == 'O' else 'Under '
                    amount = overUnder + amount[1:]

                    output += f'    {amount}: {odd} \n'
            output += '\n' 
        
        return output