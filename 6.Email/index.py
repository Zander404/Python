import smtplib


sender = "nssp@gmail.com"
receiver = "pytjon@gmail.com"
password = "password123"
subject = "Python Email test"
body = "I wrote this thing"

message = f"""From: {sender}
To:{receiver}
Subject: {subject}
{body}
 """

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try: 
    server.login(sender,password)
    print("Logged in ...")
    server.sendmail(sender,receiver,message)
    print("O email foi enviado!")

except smtplib.SMTPAuthenticationError as e:
    # print("Não posso mandar o email")
    print(e)