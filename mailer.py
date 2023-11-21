import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def mail_sender(user, password, reciver, subject, body, file):

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = reciver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    filename = file
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)

    server.sendmail(user, reciver, text)
    server.quit()
