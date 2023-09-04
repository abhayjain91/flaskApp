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


def using_sendgrid():
    import sendgrid
    import os
    from sendgrid.helpers.mail import Mail, Email, To, Content

    my_sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

    # Change to your verified sender
    from_email = Email("your_email@example.com")

    # Change to your recipient
    to_email = To("destination@example.com")

    subject = "Lorem ipsum dolor sit amet"
    content = Content("text/plain", "consectetur adipiscing elit")

    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = my_sg.client.mail.send.post(request_body=mail_json)
