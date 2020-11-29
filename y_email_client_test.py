import email, smtplib,ssl
from pathlib import Path
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "testmail@dreampeak.de"
sender_password = None
btc_price_list = []
html = """
Hello the Sun will go up at %s : %s and set at %s : %s.
"""
subject = f"Morning Sunrise - from Leon"
receiver_email = "receiver@mail.com"
f = open("password.txt", "r")
html = html % btc_price_list
sender_password = f.read()

""" Message """
message = MIMEMultipart()
message["From"]= sender_email
message["To"] = receiver_email
message["Subject"] = subject
#message.attach(MIMEText(body, "plain")) # Add body to email
message.attach(MIMEText(html, "html"))

# Add attachment to message and convert message to string
text = message.as_string()


""" Mailserver """
mailserver = smtplib.SMTP("smtp.strato.de",587)
mailserver.ehlo()
mailserver.starttls()
mailserver.login(sender_email, sender_password)
mailserver.sendmail(sender_email,receiver_email, str(text))
mailserver.quit()



