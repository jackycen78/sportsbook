import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from info import sender, receivers


def send_email(subject, content):
    
    senderAddress = sender['userEmail']
    senderPass = sender['password']
    
    message = MIMEMultipart()
    message['From'] = 'NBA Betting Odds'
    message['To'] = receivers
    message['Subject'] = subject
    message.attach(MIMEText(content, "html"))

    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls() 
    session.login(senderAddress, senderPass) 

    text = message.as_string()
    session.sendmail(senderAddress, receivers, text)
    session.quit()
    print('Mail Sent')

