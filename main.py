from utils.sendemail import sendEmail
from utils.content import getGamePropsContent
from utils.helper import getDate
from info import sender, receivers

from utils.automate.player import Pinnacle, PlayNow, Bet365
from models.allplayerprops import AllPlayerProps

from utils.website import Website

'''sendEmail(senderInfo=sender, 
senderName='Betting Odds', 
receiverAddress=receivers, 
subject= f'Game Props {getDate()}', 
content=getGamePropsContent()
)'''


site = Website()

p = Pinnacle(site)
p.automate()

q = PlayNow(site)
q.automate()

allProps = AllPlayerProps()
allProps.add_prop(p.get_player_props())
allProps.add_prop(q.get_player_props())

print(allProps)

