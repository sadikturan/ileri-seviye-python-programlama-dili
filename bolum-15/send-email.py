import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp-relay.brevo.com"
login = "<login>"
password = "<password>"

sender_email = "<email>"
receiver_email = "<email>"

# email_list = ["abc@gmail.com,xyz@gmail.com"]

text = """
    Merhaba, Bu eposta Python uygulamamdan gönderildi.
"""

message = MIMEText(text, "plain")
message["Subject"] = "Merhaba"
message["From"] = sender_email
message["To"] = receiver_email
# message["To"] = ",".join(email_list)

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(login,password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Eposta gönderildi.")