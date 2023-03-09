from utils.playernames import playNowPlayerName, sportsInteractionPlayerNames
from utils.teamnames import sportsInteractionTeamChanges

class PlayerParser():

    def __init__(self):
        pass

class PlayNowPlayerParser(PlayerParser):

    propTypes = {'Player Points + Assists + Rebounds': 'Pts + Ast + Reb', 
                 'Player Points': 'Points', 
                 'Player Assists': 'Assists',
                 'Player Rebounds': 'Rebounds', 
                 'Player Three Pointers': 'Three Pointers'}

    def __init__(self):
        super().__init__()
            
    def parseProp(self, bet):

        for type in self.propTypes:
            if bet.startswith(type) and (not bet.startswith('Player Points +') or bet.startswith('Player Points + Assists + Rebounds')):

                betInfo = bet[len(type) + 1:].split('\n')
                type = self.propTypes[type]

                player = betInfo[0]
                if player in playNowPlayerName:
                    player = playNowPlayerName[player]
                player = player.upper()

                odds = []
                for i in range(1, len(betInfo) - 1, 2):
                    amount = betInfo[i]
                    amount = 'O' + betInfo[i][:-1]
                    odd = betInfo[i + 1]

                    odds.append((amount, odd))
        
                return player, type, odds
            
        return '', '', ''

    def parseGameInfo(self, gameInfo):
        try:
            time, away, home = gameInfo.split('\n')
            time = time.split(' ')[1]
            return time, home, away
        except:
            return '', '', ''
        

class PinnaclePlayerParser(PlayerParser):
    propTypes = {'Pts+Rebs+Asts': 'Pts + Ast + Reb', 
                 'Points': 'Points', 
                 'Assists': 'Assists', 
                 'Rebounds': 'Rebounds',
                 '3 Point FG': 'Three Pointers'}

    def __init__(self):
        super().__init__()

    def parseProp(self, bet):
        
        betNameStart = bet.find('(')
        betNameEnd = bet.find(')') + 1
        last = bet.rfind(')') + 1

        player = bet[:betNameStart - 1]
        player = player.upper()
        type = bet[betNameStart + 1: betNameEnd - 1]
        info = bet[last:]

        if info and type in self.propTypes:
            info = info.split('\n')[1:]
            type = self.propTypes[type]
            
            if len(info) >= 4:

                over = 'O' + info[-4].split(' ')[1]
                overOdds = info[-3][:4]

                under = 'U' + info[-2].split(' ')[1]
                underOdds = info[-1][:4]

                odds = [(over, overOdds), 
                        (under, underOdds)]

                return player, type, odds
            
        return '', '', ''

    def parseGameInfo(self, gameInfo):
        try:
            time, away, home = gameInfo.split('\n')
            time = time.split(' ')[-1]
            return time, home, away
        except:
            return '', '', ''
        
class SportsInteractionParser(PlayerParser):
    propTypes = {'TOTAL PTS / ASSISTS / REBS': 'Pts + Ast + Reb', 
                 'TOTAL POINTS': 'Points', 
                 'TOTAL ASSISTS': 'Assists', 
                 'TOTAL REBOUNDS': 'Rebounds',
                 'TOTAL 3PT SHOTS MADE': 'Three Pointers'}

    def __init__(self):
        super().__init__()

    def parseProp(self, bet):
        
        try:
            type, info = bet.split(' - ')
            info = info.split('\n')

            if type in self.propTypes:
                type = self.propTypes[type]

                if len(info) == 5:
                    player = info[0]
                    if '[' in player:
                        bracketIndex = player.find('[') - 1
                        player = player[:bracketIndex]
                    if player in sportsInteractionPlayerNames:
                        player = sportsInteractionPlayerNames[player]
                    player = player.upper()

                    over = 'O' + info[1][4:]
                    overOdds = info[2]
                    under = 'U' + info[3][5:]
                    underOdds = info[4]

                    odds = [(over, overOdds), 
                            (under, underOdds)]
                        
                    return player, type, odds
        except:
            return '', '', ''
    
    def parseGameInfo(self, gameInfo):
        try:
            time, teams = gameInfo.split('\n')
            away, home = teams.split(' @ ')
            return time, sportsInteractionTeamChanges[home], sportsInteractionTeamChanges[away]
        except:
            return '', '', ''