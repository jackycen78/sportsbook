from utils.sendemail import sendEmail
from utils.content import getGameBetContent, getPlayerPropsContent
from utils.helper import get_date
from info import sender, receivers

from automate.player import Pinnacle, PlayNow
from models.allplayerprops import AllPlayerProps

from utils.website import Website

sendEmail(  senderInfo=sender, 
            senderName='Betting Odds', 
            receiverAddress=receivers, 
            subject= f'Test', 
            content=getPlayerPropsContent()
)