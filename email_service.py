import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = MIMEMultipart()
message["To"] = 'Me'
message["From"] = 'From flask app'
message["Subject"] = 'Test email from flask app'

title = '<b> Title line here. </b>'
messageText = MIMEText('''Message body goes here.''', 'html')
message.attach(messageText)

email = '----'
password = '----'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo('Gmail')
server.starttls()
server.login(email, password)
fromaddr = email
toaddrs = '----'
server.sendmail(fromaddr, toaddrs, message.as_string())

server.quit()
