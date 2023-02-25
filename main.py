from utils.automate import *
from utils.website import Website
from utils.sendEmail import sendEmail

from utils.allbets import AllBets
from templates.tables import *
from templates.email import *
from test import games

"""site = Website()
allBets = AllBets()

allBets.add_bets(getPlayNowBets(site))
allBets.add_bets(getSportsInteractionBets(site))
allBets.add_bets(getBet365Bets(site))
allBets.add_bets(getPinnacleBets(site))

allBets.print_bets()
games = allBets.games"""


columns = ['Game', 'PlayNow', 'Sports Interact', 'Bet365', 'Pinnacle']

moneyLinesTable = getTableHTML(titleName='Money Lines', 
                               columnNames=columns,
                               dataRows=getGamesHTML(games, moneyLineFormat))

spreadsTable = getTableHTML(titleName='Spreads', 
                            columnNames=columns,
                            dataRows=getGamesHTML(games, spreadFormat))

overUndersTable = getTableHTML(titleName='Over Unders', 
                               columnNames=columns,
                               dataRows=getGamesHTML(games, overUnderFormat))


sendEmail(getEmailHTML([moneyLinesTable,
                        spreadsTable,
                        overUndersTable,
                        ]))