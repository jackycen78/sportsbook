import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from info import sender

mail_content = 'Hello, This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library. Thank You '

senderAddress = sender['userEmail']
senderPass = sender['password']
receiverAddress = 'jackycen78@gmail.com'

message = MIMEMultipart()
message['From'] = senderAddress
message['To'] = receiverAddress
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject linepip3 

message.attach(MIMEText(mail_content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(senderAddress, senderPass) #login with mail_id and password

text = message.as_string()
session.sendmail(senderAddress, receiverAddress, text)
session.quit()
print('Mail Sent')