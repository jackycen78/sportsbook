from utils.sendemail import sendEmail
from utils.content import getGamePropsContent
from utils.helper import getDate
from info import sender, receivers

sendEmail(senderInfo=sender, 
          senderName='Betting Odds', 
          receiverAddress=receivers, 
          subject= f'Game Props {getDate()}', 
          content=getGamePropsContent()
          )