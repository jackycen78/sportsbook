from utils.sendemail import sendEmail
from utils.content import getGameBetContent
from utils.helper import getDate
from info import sender, receivers
from tests.player import get_all_props

from utils.automate.player import get_game_props

'''sendEmail(senderInfo=sender, 
senderName='Betting Odds', 
receiverAddress=receivers, 
subject= f'Game Props {getDate()}', 
content=getGameBetContent()
)
'''
#g = get_game_props()
#print(g)

print(get_all_props())