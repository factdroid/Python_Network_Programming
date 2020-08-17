import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


#Set up the server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.ehlo()

#Read in password which will be used to login
with open('password.txt', 'r') as f:
    password = f.read()

#In order for this to work, "Allow Less Secure Apps on Google Account"
server.login('factdroidtest@gmail.com', password)

#Create the message object
msg = MIMEMultipart()
msg['From'] = 'Osam'
msg['To'] = 'factsdroid@gmail.com'
msg['Subject'] = "Trying out Python Mailing Client"

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

#Get file to be attached
filename = 'random_image.jpg'
#Read-in file in bytes
attachment = open(filename, 'rb')

#Create a payload
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

#Encode the attachment
encoders.encode_base64(p)

#Add Header
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

#Get the entire email as a string
text = msg.as_string()

#Send the email
server.sendmail('factdroidtest@gmail.com', 'factsdroid@gmail.com', text)
