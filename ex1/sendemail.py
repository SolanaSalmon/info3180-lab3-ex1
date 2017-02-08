import smtplib
from_name = ''
from_addr = '@gmail.com'
to_name = 'S D'
to_addr = '@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {} 
{}
"""
subject = 'Just doing school work'
msg = 'Hey there'

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentials (if needed)
username = ''
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()