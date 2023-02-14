class AllBets:

    def __init__(self):
        self.games = {}

    def add_bets(self, bets):
        for bet in bets:
            teams = bet.get_teams()
            if teams in self.games:
                self.games[teams].append(bet)
            else:
                self.games[teams] = [bet]

    def print_bets(self):
        for team in self.games:
            for bet in self.games[team]:
                print(bet)
