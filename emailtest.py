import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from emailtemplate import template
from info import sender
from datetime import datetime

senderAddress = sender['userEmail']
senderPass = sender['password']
receiverAddress = 'jackycen78@gmail.com'

curDate = datetime.now().strftime("%B %d")
message = MIMEMultipart()
message['From'] = senderAddress
message['To'] = receiverAddress
message['Subject'] = f'NBA Odds {curDate}'
message.attach(MIMEText(template, "html"))

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(senderAddress, senderPass) #login with mail_id and password

text = message.as_string()
session.sendmail(senderAddress, receiverAddress, text)
session.quit()
print('Mail Sent')