class AllPlayerProps:

    def __init__(self):
        self.games = {}

    def add_prop(self, props):

        for prop in props:
            team = f'{prop.away} at {prop.home}'
            if team not in self.games:
                self.games[team] = {}
            
            if prop.player not in self.games[team]:
                self.games[team][prop.player] = []
            
            self.games[team][prop.player].append(prop)

    def __str__(self):
        output = ''
        for game in self.games:
            output += f'{game} \n'
            
            for player in self.games[game]:
                output += f'    {player} \n'

                for prop in self.games[game][player]:
                    output += f'        {prop.book}: {prop.type} \n'

                    '''for amount, odd in prop.odds:
                            overUnder = 'Over ' if amount[0] == 'O' else 'Under '
                            amount = overUnder + amount[1:]

                            output += f'            {amount}: {odd} \n' '''
                output += '\n' 

        return output