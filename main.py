from utils.sendemail import sendEmail
from utils.content import getGameBetContent
from utils.helper import get_date
from info import sender, receivers


'''
sendEmail(senderInfo=sender, 
          senderName='Betting Odds', 
          receiverAddress=receivers, 
          subject= f'Game Props {get_date()}', 
          content=getGameBetContent())

'''

from tests.game import get_all_test_bets

print(get_all_test_bets())