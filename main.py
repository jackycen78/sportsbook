from automate import *
from website import Website
from allbets import AllBets

site = Website()
allBets = AllBets()

allBets.add_bets(getPlayNowBets(site))
allBets.add_bets(getSportsInteractionBets(site))
allBets.add_bets(getBet365Bets(site))

games = allBets.games