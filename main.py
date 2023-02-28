from utils.sendemail import sendEmail
from utils.content import getGamePropsContent
from utils.helper import getDate
from info import sender, receivers

from utils.automate.player import pinnaclePlayerProps, playNowPlayerProps, bet365PlayerProps
from utils.website import Website

'''sendEmail(senderInfo=sender, 
          senderName='Betting Odds', 
          receiverAddress=receivers, 
          subject= f'Game Props {getDate()}', 
          content=getGamePropsContent()
          )
'''
bet365PlayerProps(Website())