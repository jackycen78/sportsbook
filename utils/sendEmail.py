import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from info import sender
from datetime import datetime

def sendEmail(content):
    
    senderAddress = sender['userEmail']
    senderPass = sender['password']
    receiverAddress = 'jackycen78@gmail.com'

    curDate = datetime.now().strftime("%B %d")
    message = MIMEMultipart()
    message['From'] = 'Betting Odds'
    message['To'] = receiverAddress
    message['Subject'] = f'NBA Odds {curDate}'
    message.attach(MIMEText(content, "html"))

    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls() 
    session.login(senderAddress, senderPass) 

    text = message.as_string()
    session.sendmail(senderAddress, receiverAddress, text)
    session.quit()
    print('Mail Sent')