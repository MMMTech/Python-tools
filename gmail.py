import smtplib
import imaplib
import email
from email.header import decode_header
import getpass

class MT_Mail:

    def __init__(self, user_email, to_email, password):
        self.flags = {'unread': '(UNSEEN)', 'all': '(ALL)'}
        self.user_email = user_email
        self.to_email = to_email
        self.password = password
        (self.server, self.port) = self._server()

    def _server(self, server="smtp.gmail.com" , port=587):
        self.server = server
        self.port = port
        return (self.server, self.port)

    def send_mail(self, msg):
        try:
            (server, port) = self._server()
            mail_server = smtplib.SMTP(server, port)
            mail_server.ehlo()
            mail_server.starttls()
            mail_server.ehlo()
            islogged_in = mail_server.login(self.user_email, self.password)
            mail_server.sendmail(self.user_email, self.to_email, msg)
            mail_server.close()

            #Debugging
            #print("[+] Authentication Succefull.")
            return islogged_in

        except smtplib.SMTPAuthenticationError:
            # Debugging
            #print("[-] Authentication failed.")
            return ("[-] Smtp Authentication failed.", False)

    def get_emails(self, flag='all'):
        flag = self.flags[flag]
        # Connect to the server and login
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(self.user_email, self.password)

        # Select the mailbox you want (in this case, the inbox)
        mail.select("inbox")

        # Search for all emails that are "unseen" (unread)
        status, messages = mail.search(None, flag)

        for id in messages[0].split():
            # Fetch the email by its unique ID
            status, msg_data = mail.fetch(id, '(RFC822)')

            # Get the email content
            msg = email.message_from_bytes(msg_data[0][1])

            # Decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                if encoding:
                    subject = subject.decode(encoding)
                else:
                    subject = subject.decode('utf-8')

            # Get the sender's email
            from_ = email.utils.parseaddr(msg["From"])[1]

            print("Subject:", subject)
            file_subject = "Subject: " + subject
            print("From:", from_)
            file_from = "From: " + from_
            print("-" * 50)
            seperator_dash = "-" * 50

            # If the email is a multipart, extract the main content
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    # skip any text/plain (txt) attachments
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        body = part.get_payload(decode=True).decode()
                        print(body)
                        file_body = body
            else:
                body = msg.get_payload(decode=True).decode()
                print(body)
                file_body = body


            print("=" * 100)
            seperator_equal = "=" * 100

        # Logout and close the connection
        mail.logout()

    def get_email_folders(self):
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(self.user_email, self.password)
        return mail.list()

    def get_flag(self):
        return self.flags


#lrecrssjzhuroytk
#python.botx9@gmail.com
user_email = "Python.botx9@gmail.com"
#from_email = "AlienElite@anotherplanet.com"
to_email = "Python.botx9@gmail.com"
#to_email = "sarahamanda999@gmail.com"
password = "lrecrssjzhuroytk"
email_folder = "inbox"

subject = "Testing 123"
body = "Alien Elite bot testing..."
message = "Subject: " + subject + "\n" + body

server = MT_Mail(user_email, to_email, password)
#server.send_mail(message)
#server.get_emails('unread')
server.get_emails()



