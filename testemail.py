from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'gkerry200@gmail.com'
email_password = 'shtwihosbkfmshll'
email_receiver = 'gkerry200@gmail.com'

subject = 'Check out new ticket'
body = """ I have just sent my first ticket!"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
