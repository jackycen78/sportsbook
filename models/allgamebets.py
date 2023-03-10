class AllBets:

    def __init__(self):
        self.games = {}

    def add_bets(self, bets):
        for bet in bets:
            teams = bet.get_teams()
            if teams not in self.games:
                self.games[teams] = []
            self.games[teams].append(bet)
        
    def __str__(self):
        output = ''
        for team in self.games:
            output += f'{team}\n'
            for bet in self.games[team]:
                output += f'   {bet.book}\n'
                
            output += '\n'
        return output
