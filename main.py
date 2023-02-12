from automate import *
from website import Website
from allbets import AllBets

site = Website()
allBets = AllBets()

allBets.addBet(getSportsInteractionBets(site))
allBets.addBet(getPlayNowBets(site))
#allBets.addBet(getBet365Bets(site))

allBets.printBets()

