import credentials 
import smtplib
from email.mime.text import MIMEText

def send(to, subject, message):
	smtp_ssl_host = 'smtp.gmail.com' 
	smtp_ssl_port = 465
	username = credentials.user
	password = credentials.password
	targets = to
	sender = 'BOT'

	msg = MIMEText(message)
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = ', '.join(targets)

	server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
	server.login(username, password)
	server.sendmail(sender, targets, msg.as_string())
	server.quit()