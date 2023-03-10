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
    
    def change_american_odds(self, data):
        if len(data) == 2:
            return [decimal_to_american(data[0]),
                    decimal_to_american(data[1])]
        
        elif len(data) == 4:
            return [data[0],
                    decimal_to_american(data[1]),
                    data[2],
                    decimal_to_american(data[3]),
                    ]

class PlayNow(GameParser):

    def __init__(self):
        super().__init__()

    def parse_teams(self, teamInfo):
        if teamInfo:
            return teamInfo.split('\n')
        return self.emptyTeams

    def parse_spreads(self, spreadInfo):
        if spreadInfo:
            return self.change_american_odds(spreadInfo.split('\n'))
        return self.emptySpreads

    def parse_money_lines(self, moneyLineInfo):
        if moneyLineInfo:
            moneyLineInfo = moneyLineInfo.split('\n')
            moneyLines = [moneyLineInfo[1], 
                          moneyLineInfo[3]]
            return self.change_american_odds(moneyLines)
        return self.emptyMoneyLines
    
    def parse_over_unders(self, overUnderInfo):
        if overUnderInfo:
            overUnderInfo = overUnderInfo.split('\n')
            overUnders = [overUnderInfo[1], 
                          overUnderInfo[2], 
                          overUnderInfo[4], 
                          overUnderInfo[5]]
            return self.change_american_odds(overUnders)
        return self.emptyOverUnders

class Pinnacle(GameParser):

    def __init__(self):
        super().__init__()

    def parse_teams(self, teamInfo):
        if teamInfo and len(teamInfo.split('\n')) == 3:
            awayTeam, homeTeam, gameTime = teamInfo.split('\n')
            return [awayTeam, homeTeam]
        return self.emptyTeams

    def parse_spreads(self, spreadInfo):
        if spreadInfo and len(spreadInfo.split('\n')) == 4:
            return self.change_american_odds(spreadInfo.split('\n'))
        return self.emptySpreads
    
    def parse_money_lines(self, moneyLineInfo):
        if moneyLineInfo and len(moneyLineInfo.split('\n')) == 2:
            return self.change_american_odds(moneyLineInfo.split('\n'))
        return self.emptyMoneyLines
    
    def parse_over_unders(self, overUnderInfo):
        if overUnderInfo and len(overUnderInfo.split('\n')) == 4:
            return self.change_american_odds(overUnderInfo.split('\n'))
        return self.emptyOverUnders
        
class Bet365(GameParser):
    def __init__(self):
           super().__init__()

    def parse_teams(self, teamInfo):
        if teamInfo:
            return [getBet365TeamName(team) for team in teamInfo.split('\n')]
        return self.emptyTeams

    def parse_spreads(self, spreadInfo):
        if spreadInfo and len(spreadInfo[0].split('\n')) == 2:
            return flatten([spread.split('\n') for spread in spreadInfo])
        return self.emptySpreads

    def parse_money_lines(self, moneyLineInfo):
        if moneyLineInfo:
            return moneyLineInfo
        return self.emptyMoneyLines
        
    def parse_over_unders(self, overUnderInfo):
        if overUnderInfo and len(overUnderInfo[0].split('\n')) == 2:
            overUnders = flatten([ou.text.split('\n') for ou in overUnderInfo])
            overUnders[0] = overUnders[0][2:]
            overUnders[2] = overUnders[2][2:]
            return overUnders
        return self.emptyOverUnders

class SportsInteract(GameParser):

    def __init__(self):
        super().__init__()

    def parse_teams(self, teamInfo):
        if teamInfo:
            teams = teamInfo.split(' ')
            atIndex = teams.index('@')
            awayTeam = " ".join(teams[0: atIndex])
            homeTeam = " ".join(teams[atIndex + 1:])
            awayTeam = getSportsIntTeamName(awayTeam)
            homeTeam = getSportsIntTeamName(homeTeam)

            return [awayTeam, homeTeam]
        return self.emptyTeams

    def parse_spreads(self, spreadInfo):
        if spreadInfo and len(spreadInfo.split('\n')) == 5 and 'Closed' not in spreadInfo:
            return self.change_american_odds(spreadInfo.split('\n')[1:])
        return self.emptySpreads

    def parse_money_lines(self, moneyLineInfo):
        if moneyLineInfo and 'Closed' not in moneyLineInfo:
            return self.change_american_odds(moneyLineInfo.split('\n')[1:])
        return self.emptyMoneyLines
    
    def parse_over_unders(self, overUnderInfo):
        if overUnderInfo and 'Closed' not in overUnderInfo:
            overUnders = overUnderInfo.split('\n')[1:]

            over = overUnders[1]
            overOdds = decimal_to_american(overUnders[2])
            under = overUnders[4]
            underOdds = decimal_to_american(overUnders[5])

            return self.change_american_odds([over,
                                              overOdds,
                                              under,
                                              underOdds])
        return self.emptyOverUnders

