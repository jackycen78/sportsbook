from utils.bet import *
from utils.allbets import AllBets

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
testBet365Bet1.overUnder = {'over': '250.0',
                            'overOdds': '2.05',
                            'under': '235.0',
                            'underOdds': '1.89',
                            }

testBet365Bet2 = Bet365Bet(['', '', '', ''])
testBet365Bet2.teams = {'home': 'Brooklyn Nets',
                        'away': 'Miami Heat',
                        }

testBet365Bet2.spread = {'homeSpread' : '+19.5',
                         'homeSpreadOdds' : '1.90', 
                         'awaySpread' : '-19.5',
                         'awaySpreadOdds' : '1.90',
                         }

testBet365Bet2.moneyLine = {'homeMoneyLine' : '1.02',
                            'awayMoneyLine' : '17.67',
                            }

testBet365Bet2.overUnder = {'over': '250.0',
                            'overOdds': '2.05',
                            'under': '235.0',
                            'underOdds': '1.89',
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

testPlayNowBet2 = PlayNowBet(['', '', '', ''])
testPlayNowBet2.teams = {'home': 'Brooklyn Nets',
                        'away': 'Miami Heat',
                        }

testPlayNowBet2.spread = {'homeSpread' : '+18.5',
                         'homeSpreadOdds' : '1.90', 
                         'awaySpread' : '-18.5',
                         'awaySpreadOdds' : '1.90',
                         }

testPlayNowBet2.moneyLine = {'homeMoneyLine' : '1.20',
                            'awayMoneyLine' : '15.67',
                            }

testPlayNowBet2.overUnder = {'over': '247.0',
                            'overOdds': '2.01',
                            'under': '247.0',
                            'underOdds': '1.98',
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

testSportsIntBet2 = Bet365Bet(['', '', '', ''])
testSportsIntBet2.teams = {'home': 'Brooklyn Nets',
                            'away': 'Miami Heat',
                        }

testSportsIntBet2.spread = {'homeSpread' : '+21.5',
                         'homeSpreadOdds' : '1.90', 
                         'awaySpread' : '-21.5',
                         'awaySpreadOdds' : '1.90',
                         }

testSportsIntBet2.moneyLine = {'homeMoneyLine' : '1.15',
                            'awayMoneyLine' : '17.67',
                            }

testSportsIntBet2.overUnder = {'over': '217.0',
                            'overOdds': '1.98',
                            'under': '217.0',
                            'underOdds': '2.08',
                            }

testPinnacleBet1 = PinnacleBet(['', '', '', ''])
testPinnacleBet1.teams = {'home': 'Utah Jazz',
                           'away': 'Toronto Raptors',
                          }

testPinnacleBet1.spread = {'homeSpread' : '+9.5',
                           'homeSpreadOdds' : '1.90',
                           'awaySpread' : '-9.5',
                           'awaySpreadOdds' : '1.90',
                          }

testPinnacleBet1.moneyLine = {'homeMoneyLine' : '1.66',
                             'awayMoneyLine' : '2.52',
                            }

testPinnacleBet1.overUnder = {'over': '233.0',
                             'overOdds': '2.01',
                             'under': '233.0',
                             'underOdds': '1.85',
                            }

testPinnacleBet2 = PinnacleBet(['', '', '', ''])
testPinnacleBet2.teams = {'home': 'Brooklyn Nets',
                            'away': 'Miami Heat',
                        }

testPinnacleBet2.spread = {'homeSpread' : '+21.5',
                         'homeSpreadOdds' : '1.90', 
                         'awaySpread' : '-21.5',
                         'awaySpreadOdds' : '1.90',
                         }

testPinnacleBet2.moneyLine = {'homeMoneyLine' : '1.15',
                            'awayMoneyLine' : '17.67',
                            }

testPinnacleBet2.overUnder = {'over': '217.0',
                            'overOdds': '1.98',
                            'under': '217.0',
                            'underOdds': '2.08',
                            }

allBets = AllBets()
allBets.add_bets([testPlayNowBet1, testPlayNowBet2])
allBets.add_bets([testSportsIntBet1, testSportsIntBet2])
allBets.add_bets([testBet365Bet1, testBet365Bet2])
allBets.add_bets([testPinnacleBet1, testPinnacleBet2])

games = allBets.games