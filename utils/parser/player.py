
class PlayerParser():

    def __init__(self, games):
        self.games = games


class PlayNowPlayerParser(PlayerParser):
    propTypes = ['Player Points + Assists + Rebounds', 'Player Points', 'Player Assists', 'Player Rebounds', 'Player Three Pointers']

    def __init__(self, games):
        super().__init__(games)

    def parseAll(self):
        for game in self.games:
            for bet in game:
                for type in self.propTypes: 
                    if bet.startswith(type):
                        if bet.startswith('Player Points +') and not bet.startswith('Player Points + Assists + Rebounds'):
                            pass
                        else:
                            self.parseProp(bet, type)
                            break
            

    def parseProp(self, bet, type):
        betInfo = bet[len(type) + 1:].split('\n')

        player = betInfo[0]
        odds = []
        for i in range(1, len(betInfo) - 1, 2):
            odds.append((betInfo[i], betInfo[i+1]))
        print(f'{player}: {odds}')