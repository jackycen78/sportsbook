from utils.automate import *
from utils.website import Website
from utils.sendemail import sendEmail
from models.allbets import AllBets
from templates.tables import *
from templates.email import *
from tests.test import games
from info import sender, receivers

from datetime import datetime

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

content = [moneyLinesTable,
           spreadsTable,
           overUndersTable,
           ]

contentHTML = getEmailHTML(content)

sendEmail(senderInfo=sender, 
          senderName='Betting Odds', 
          receiverAddress=receivers, 
          subject=datetime.now().strftime("%B %d"), 
          content=contentHTML)