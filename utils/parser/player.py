from utils.names.player import getPlayNowPlayerName, getSportsInteractPlayerName, getPinnaclePlayerName, getFullTeam
from utils.helper import decimal_to_american

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
            
    def parse_prop(self, bet):
        for type in self.propTypes:
            if self.valid_prop(bet, type):
                playerInfo, oddsInfo = bet[len(type) + 1:].split('\n', 1)
                type = self.parse_type(type)
                player = self.parse_player(playerInfo)
                odds = self.parse_odds(oddsInfo)
                return player, type, odds
        return '', '', ''
    
    def valid_prop(self, bet, type):
        return bet.startswith(type) and (not bet.startswith('Player Points +') or bet.startswith('Player Points + Assists + Rebounds'))
    
    def parse_type(self, propType):
        return self.propTypes[propType]
    
    def parse_player(self, playerInfo):
        return getPlayNowPlayerName(playerInfo)
    
    def parse_odds(self, oddsInfo):
        odds = []
        oddsInfo = oddsInfo.split('\n')

        for i in range(0,len(oddsInfo) - 1, 2):
            amount = 'O' + oddsInfo[i][:-1]
            odd = decimal_to_american(oddsInfo[i + 1])
            odds.append((amount, odd))
        return odds

    def parse_game_info(self, gameInfo):
        time, away, home = gameInfo.split('\n')
        return time, home, away
        
        

class PinnaclePlayerParser(PlayerParser):
    propTypes = {'Pts+Rebs+Asts': 'Pts + Ast + Reb', 
                 'Points': 'Points', 
                 'Assists': 'Assists', 
                 'Rebounds': 'Rebounds',
                 '3 Point FG': 'Three Pointers'}

    def __init__(self):
        super().__init__()

    def parse_prop(self, bet):
        
        typeStart = bet.find('(')
        typeEnd = bet.find(')')
        infoStart = bet.rfind(')') + 1

        playerInfo = bet[:typeStart - 1]
        typeInfo = bet[typeStart + 1: typeEnd]
        oddsInfo = bet[infoStart:].split('\n')[1:]

        if self.valid_prop(typeInfo, oddsInfo):

            type = self.parse_type(typeInfo)
            player = self.parse_player(playerInfo)
            odds = self.parse_odds(oddsInfo)
            return player, type, odds
            
        return '', '', ''


    def valid_prop(self, type, info):
        return type in self.propTypes and len(info) >= 4
    
    def parse_type(self, propType):
        return self.propTypes[propType]
    
    def parse_player(self, playerInfo):
        return playerInfo
    
    def parse_odds(self, oddsInfo):
        over = 'O' + oddsInfo[-4].split(' ')[1]
        overOdds = decimal_to_american(oddsInfo[-3][:4])
        under = 'U' + oddsInfo[-2].split(' ')[1]
        underOdds = decimal_to_american(oddsInfo[-1][:4])

        odds = [(over, overOdds), 
                (under, underOdds)]
        return odds
    
    def parse_game_info(self, gameInfo):

        time, away, home = gameInfo.split('\n')
        time = time.split(' ')[-1]
        return time, home, away
      
        
class SportsInteractParser(PlayerParser):
    propTypes = {'TOTAL PTS / ASSISTS / REBS': 'Pts + Ast + Reb', 
                 'TOTAL POINTS': 'Points', 
                 'TOTAL ASSISTS': 'Assists', 
                 'TOTAL REBOUNDS': 'Rebounds',
                 'TOTAL 3PT SHOTS MADE': 'Three Pointers'}

    def __init__(self):
        super().__init__()

    def parse_prop(self, bet):
    
        type, info = bet.split(' - ')
        info = info.split('\n')

        if self.valid_prop(type, info):
            playerInfo = info[0]
            oddsInfo = info[1:]

            type = self.parse_type(type)
            player = self.parse_player(playerInfo)
            odds = self.parse_odds(oddsInfo)

            return player, type, odds
        
        return '', '', ''
    
    def valid_prop(self, type, info):
        return type in self.propTypes and len(info) == 7
    
    def parse_type(self, propType):
        return self.propTypes[propType]
    
    def parse_player(self, playerInfo):
        player = playerInfo
        if '[' in player:
                    bracketIndex = player.find('[') - 1
                    player = player[:bracketIndex]

        return getSportsInteractPlayerName(player)
    
    def parse_odds(self, oddsInfo):
        over = 'O' + oddsInfo[1]
        overOdds = decimal_to_american(oddsInfo[2])
        under = 'U' + oddsInfo[4]
        underOdds = decimal_to_american(oddsInfo[5])
        odds = [(over, overOdds), 
                (under, underOdds)]
        return odds
    
    def parse_game_info(self, gameInfo):
        time, teams = gameInfo.split('\n')
        away, home = teams.split(' @ ')
        return time, getFullTeam(home), getFullTeam(away)
    