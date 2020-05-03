import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

EMAIL = config.EMAIL
PASSWORD = config.PASSWORD

server.login(EMAIL, PASSWORD)

message = msg = MIMEMultipart('alternative')
message['From'] = EMAIL
message['To'] = EMAIL
message['Subject'] = 'Python Message'

# Create the body of the message (a plain-text and an HTML version).
text = 'Good Day Surajit,\nThis is an automated message from Python.\nRegards,\nPython Messenger'
html = """\
<html>
  <head>Sent from Python</head>
  <body>
    <p>Good Day Surajit,<br></p><br/>
    <p>This is an automated message from Python</p>
    <p>Regards,</p>
    <p>Python Messenger</p><br/>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
message.attach(part1)
message.attach(part2)

server.sendmail(EMAIL, EMAIL, message.as_string())

print('Mail has been sent successfully')