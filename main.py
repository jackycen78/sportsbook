from utils.sendemail import sendEmail
from info import sender, receivers
from utils.content import getGamePropsContent

from datetime import datetime

contentHTML = getGamePropsContent()

sendEmail(senderInfo=sender, 
          senderName='Betting Odds', 
          receiverAddress=receivers, 
          subject=datetime.now().strftime("%B %d"), 
          content=contentHTML)