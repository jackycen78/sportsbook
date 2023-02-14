from bet import *
from allbets import AllBets

testBet365Bet1 = Bet365Bet(['', '', '', ''])
testBet365Bet1.teams = {'home': 'Utah Jazz',
                        'away': 'Toronto Raptors',
                        }

testBet365Bet1.spread = {'homeSpread' : '+9.5',
                         'homeSpreadOdds' : '1.90', 
                         'awaySpread' : '-9.5',
                         'awaySpreadOdds' : '1.90',
                         }

testBet365Bet1.moneyLine = {'homeMoneyLine' : '1.36',
                            'awayMoneyLine' : '3.25',
                            }

testBet365Bet1.overUnder = {'over': '232.0',
                            'overOdds': '2.01',
                            'under': '232.0',
                            'underOdds': '1.79',
                            }

testPlayNowBet1 = PlayNowBet(['', '', '', ''])
testPlayNowBet1.teams = {'home': 'Utah Jazz',
                         'away': 'Toronto Raptors',
                        }


testPlayNowBet1.spread = {'homeSpread' : '+9.0',
                          'homeSpreadOdds' : '1.90',
                          'awaySpread' : '-9.0',
                          'awaySpreadOdds' : '1.90',
                         }

testPlayNowBet1.moneyLine = {'homeMoneyLine' : '1.56',
                             'awayMoneyLine' : '2.98',
                            }

testPlayNowBet1.overUnder = {'over': '231.0',
                             'overOdds': '2.11',
                             'under': '231.0',
                             'underOdds': '1.75',
                            }

testSportsIntBet1 = SportsInteractionBet(['', '', '', ''])
testSportsIntBet1.teams = {'home': 'Utah Jazz',
                           'away': 'Toronto Raptors',
                          }


testSportsIntBet1.spread = {'homeSpread' : '+9.5',
                           'homeSpreadOdds' : '1.90',
                           'awaySpread' : '-9.5',
                           'awaySpreadOdds' : '1.90',
                          }

testSportsIntBet1.moneyLine = {'homeMoneyLine' : '1.66',
                             'awayMoneyLine' : '2.52',
                            }

testSportsIntBet1.overUnder = {'over': '233.0',
                             'overOdds': '2.01',
                             'under': '233.0',
                             'underOdds': '1.85',
                            }

listOfBets = [testBet365Bet1, testPlayNowBet1, testSportsIntBet1]