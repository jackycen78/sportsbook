from utils.sendemail import sendEmail
from utils.content import getGameBetContent
from utils.helper import get_date

from info import sender, receivers
from tests.player import get_all_props
from tests.game import get_all_games

from automate.player import get_game_props


'''sendEmail(senderInfo=sender, 
senderName='Betting Odds', 
receiverAddress=receivers, 
subject= f'Game Props {get_date()}', 
content=getGameBetContent()
)'''

#g = get_game_props()
#print(g)

print(get_all_props())

#k = get_all_games()
#print(k)