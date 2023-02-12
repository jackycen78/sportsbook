class AllBets:

    def __init__(self):
        self.betlist = []

    def addBet(self, bets):
        self.betlist += bets

    def printBets(self):
        for bet in self.betlist:
            print(bet)