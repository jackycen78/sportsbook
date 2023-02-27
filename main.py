from utils.sendemail import sendEmail
from info import sender, receivers
from utils.content import getGamePropsContent

from datetime import datetime

sendEmail(senderInfo=sender, 
          senderName='Betting Odds', 
          receiverAddress=receivers, 
          subject= f'Game Props {datetime.now().strftime("%B %d")}', 
          content=getGamePropsContent()
          )