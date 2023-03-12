from utils.sendemail import sendEmail
from content.game import getGameBetContent
from content.player import getPlayerPropsContent
from utils.helper import get_date
from info import sender, receivers

playerContent = getPlayerPropsContent()
gameContent = getGameBetContent()

contents = [(f'Player Props {get_date()}', playerContent),
           (f'Game Props {get_date()}', gameContent),]

def send(sub, cont):
    sendEmail(senderInfo=sender, 
              senderName='Betting Odds', 
              receiverAddress=receivers, 
              subject=sub, 
              content=cont)
    
for sub, cont in contents:
    send(sub, cont)
