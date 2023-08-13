import smtplib
import argparse
import getpass

parser = argparse.ArgumentParser()
parser.add_argument("-smpt", "--smtp-server", dest="server", help="Mail server example: smtp.gmail.com")
parser.add_argument("-p", "--port", dest="port", help="Server port example: 587 (gmail)")
parser.add_argument("-m", "--message", dest="message", help="Message to send")
parser.add_argument("-s", "--subject", dest="subject", help="Email subject")
parser.add_argument("-x", "--password", dest="password", help="Password to server login")
parser.add_argument("-u", "--user-email", dest="user_email", help="User email to login on server")
parser.add_argument("-f", "--from-email", dest="from_email", help="From email")
parser.add_argument("-t", "--to-email", dest="to_email", help="To email")
options = parser.parse_args()
def send_mail(from_email, user_email, to_email, message):
    mail_server = smtplib.SMTP(options.server, options.port)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(user_email, options.password)
    mail_server.sendmail(from_email, to_email, message)

subject = options.subject
message = "Subject: " + subject + "\n" + options.message
try:
    send_mail(options.from_email, options.user_email, options.to_email, message)
    print("[+] Email Succefully Sent")
except:
    print("[-] Email not Sent")
