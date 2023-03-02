from utils.sendemail import sendEmail
from utils.content import getGamePropsContent
from utils.helper import getDate
from info import sender, receivers

from utils.automate.player import Pinnacle, PlayNow, Bet365
from utils.website import Website

'''sendEmail(senderInfo=sender, 
        senderName='Betting Odds', 
        receiverAddress=receivers, 
        subject= f'Game Props {getDate()}', 
        content=getGamePropsContent()
        )'''

site = Website()
#pinnaclePlayerProps(site)
p = PlayNow(site)
p.automate()
print(p.playerProps)