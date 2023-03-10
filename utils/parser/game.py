from utils.names.game import getBet365TeamName, getSportsIntTeamName
from utils.helper import zip_data, flatten, decimal_to_american


class GameParser():
    emptyTeams = ['', '']
    emptySpreads = ['', '', '', '']
    emptyMoneyLines = ['', '']
    emptyOverUnders = ['', '', '', '']

    def __init__(self):
        pass

    def parse_game(self, data):
        teamInfo, spreadInfo, moneyLineInfo, overUnderInfo = data
        return zip_data(self.parse_teams(teamInfo),
                        self.parse_spreads(spreadInfo),
                        self.parse_money_lines(moneyLineInfo),
                        self.parse_over_unders(overUnderInfo),
                        )

class PlayNow(GameParser):

    def __init__(self):
        super().__init__()

    def parse_teams(self, teamInfo):
        if teamInfo:
            return teamInfo.text.split('\n')
        return self.emptyTeams

    def parse_spreads(self, spreadInfo):
        if spreadInfo:
            return spreadInfo.text.split('\n')
        return self.emptySpreads

    def parse_money_lines(self, moneyLineInfo):
        if moneyLineInfo:
            moneyLineInfo = moneyLineInfo.text.split('\n')
            moneyLines = [moneyLineInfo[1], 
                          moneyLineInfo[3]]
            return moneyLines
        return self.emptyMoneyLines
    
    def parse_over_unders(self, overUnderInfo):
        if overUnderInfo:
            overUnderInfo = overUnderInfo.text.split('\n')
            overUnders = [overUnderInfo[1], 
                        overUnderInfo[2], 
                        overUnderInfo[4], 
                        overUnderInfo[5]]
            return overUnders
        return self.emptyOverUnders

class Pinnacle(GameParser):

    def __init__(self):
        super().__init__()

    def parse_teams(self, teamInfo):
        if teamInfo and len(teamInfo.text.split('\n')) == 3:
            awayTeam, homeTeam, gameTime = teamInfo.text.split('\n')
            return [awayTeam, homeTeam]
        return self.emptyTeams

    def parse_spreads(self, spreadInfo):
        if spreadInfo and len(spreadInfo.text.split('\n')) == 4:
            return spreadInfo.text.split('\n')
        return self.emptySpreads
    
    def parse_money_lines(self, moneyLineInfo):
        if moneyLineInfo and len(moneyLineInfo.text.split('\n')) == 2:
            return moneyLineInfo.text.split('\n')
        return self.emptyMoneyLines
    
    def parse_over_unders(self, overUnderInfo):
        if overUnderInfo and len(overUnderInfo.text.split('\n')) == 4:
            return overUnderInfo.text.split('\n')
        return self.emptyOverUnders
        
class Bet365(GameParser):
    def __init__(self):
           super().__init__()

    def parse_teams(self, teamInfo):
        if teamInfo:
            return [getBet365TeamName(team) for team in teamInfo.text.split('\n')]
        return self.emptyTeams

    def parse_spreads(self, spreadInfo):
        if spreadInfo and len(spreadInfo[0].text.split('\n')) == 2:
            return flatten([spread.text.split('\n') for spread in spreadInfo])
        return self.emptySpreads

    def parse_money_lines(self, moneyLineInfo):
        if moneyLineInfo:
            return [ml.text for ml in moneyLineInfo]
        return self.emptyMoneyLines
        
    def parse_over_unders(self, overUnderInfo):
        if overUnderInfo and len(overUnderInfo[0].text.split('\n')) == 2:
            overUnders = flatten([ou.text.split('\n') for ou in overUnderInfo])
            overUnders[0] = overUnders[0][2:]
            overUnders[2] = overUnders[2][2:]
            return overUnders
        return self.emptyOverUnders

class SportsInteraction(GameParser):

    def __init__(self):
        super().__init__()

    def parse_teams(self, teamInfo):
        if teamInfo:
            teams = teamInfo.text.split(' ')
            atIndex = teams.index('@')
            awayTeam = " ".join(teams[0: atIndex])
            homeTeam = " ".join(teams[atIndex + 1:])
            awayTeam = getSportsIntTeamName(awayTeam)
            homeTeam = getSportsIntTeamName(homeTeam)

            return [awayTeam, homeTeam]
        return self.emptyTeams

    def parse_spreads(self, spreadInfo):
        if spreadInfo and len(spreadInfo.text.split('\n')) == 5 and 'Closed' not in spreadInfo.text:
            return spreadInfo.text.split('\n')[1:]
        return self.emptySpreads

    def parse_money_lines(self, moneyLineInfo):
        if moneyLineInfo and 'Closed' not in moneyLineInfo.text:
            return moneyLineInfo.text.split('\n')[1:]
        return self.emptyMoneyLines
    
    def parse_over_unders(self, overUnderInfo):
        if overUnderInfo and 'Closed' not in overUnderInfo.text:
            overUnders = overUnderInfo.text.split('\n')[1:]
            overUnders[0] = overUnders[0][1:]
            overUnders[2] = overUnders[2][1:]
            return overUnders
        return self.emptyOverUnders

