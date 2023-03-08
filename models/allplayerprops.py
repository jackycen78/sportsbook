class AllPlayerProps:

    def __init__(self):
        self.games = {}

    def add_prop(self, props):

        for prop in props:
            team = f'{prop.away} at {prop.home}'
            if team not in self.games:
                self.games[team] = {}
            
            if prop.player not in self.games[team]:
                self.games[team][prop.player] = {}
            
            if prop.type not in self.games[team][prop.player]:
                self.games[team][prop.player][prop.type] = {}

            self.games[team][prop.player][prop.type][prop.book] = prop

    def __str__(self):
        output = ''
        for game in self.games:
            if game == ' at ':
                curGame = self.games[game]
                output += f'{game} \n'
                
                for player in curGame:
                    curPlayer = curGame[player]
                    output += f'    {player} \n'

                    for type in curPlayer:
                        curType = curPlayer[type]
                        #output += f'        {type} \n'

                        for prop in curType:
                            curProp = curType[prop]
                            output += f'            {curProp.book}\n'

                            '''for amount, odd in prop.odds:
                                    overUnder = 'Over ' if amount[0] == 'O' else 'Under '
                                    amount = overUnder + amount[1:]

                                    output += f'            {amount}: {odd} \n' '''
                    output += '\n' 

        return output