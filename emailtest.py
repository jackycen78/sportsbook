from utils.sendemail import sendEmail
from utils.content import getGameBetContent
from utils.helper import getDate
from info import sender, receivers

from utils.automate.player import Pinnacle, PlayNow, Bet365
from models.allplayerprops import AllPlayerProps

from utils.website import Website

sendEmail(  senderInfo=sender, 
            senderName='Betting Odds', 
            receiverAddress=receivers, 
            subject= f'Test', 
            content=getGameBetContent()
)