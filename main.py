from utils.sendemail import sendEmail
from utils.content import getGamePropsContent
from utils.helper import getDate
from info import sender, receivers

from utils.automate.player import Pinnacle, PlayNow, Bet365
from utils.website import Website

sendEmail(senderInfo=sender, 
senderName='Betting Odds', 
receiverAddress=receivers, 
subject= f'Game Props {getDate()}', 
content=getGamePropsContent()
)


'''site = Website()
p = Pinnacle(site)
p.automate()

q = PlayNow(site)
q.automate

for f in p.playerProps:
    print(f)

for k in q.playerProps:
    print(k)'''