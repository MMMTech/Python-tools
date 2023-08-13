import smtplib
import getpass

class MT_Mail:

    def __init__(self, from_email, to_email, password):
        self.from_email = from_email
        self.to_email = to_email
        self.password = password
        (self.server, self.port) = self._server()

    def _server(self, server="smtp.gmail.com" , port=587):
        self.server = server
        self.port = port
        return (self.server, self.port)

    def send_mail(self, msg):
        (server, port) = self._server()
        mail_server = smtplib.SMTP(server, port)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(self.from_email, self.password)
        mail_server.sendmail(self.from_email, self.to_email, msg)
        mail_server.close()

#lrecrssjzhuroytk
#python.botx9@gmail.com
from_email = "Python.botx9@gmail.com"
#to_email = "Python.botx9@gmail.com"
to_email = "sarahamanda999@gmail.com"
password = "lrecrssjzhuroytk"
subject = "Regards, sincerely Your ALien:)"
body = "Next time you'll receive 100.000.000 emails!"
message = "Subject: " + subject + "\n" + body

server = MT_Mail(from_email, to_email, password)
server.send_mail(message)



