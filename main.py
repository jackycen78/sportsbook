from utils.sendemail import sendEmail
from utils.content import getGameBetContent
from utils.helper import get_date

from info import sender, receivers
from tests.game import parse_book, create_book_bet

from automate.player import get_game_props

from automate.game import PlayNow, SportsInteract, Pinnacle, GameBets
from utils.website import Website


site = Website()
s = GameBets(site)
print(s.get_all_bets())

'''sendEmail(senderInfo=sender, 
senderName='Betting Odds', 
receiverAddress=receivers, 
subject= f'Game Props {get_date()}', 
content=getGameBetContent()
)
'''
#g = get_game_props()
#print(g)

#print(get_all_props())

#k = get_all_games()
#print(k)