import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(senderInfo, senderName, receiverAddress, subject, content):
    
    senderAddress = senderInfo['userEmail']
    senderPass = senderInfo['password']
    
    message = MIMEMultipart()
    message['From'] = senderName
    message['To'] = receiverAddress
    message['Subject'] = subject
    message.attach(MIMEText(content, "html"))

    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls() 
    session.login(senderAddress, senderPass) 

    text = message.as_string()
    session.sendmail(senderAddress, receiverAddress, text)
    session.quit()
    print('Mail Sent')