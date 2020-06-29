import smtplib

TO = 'recipient@mailservice.com'
SUBJECT = 'website down'
TEXT = 'Your website is not working properly'

# Gmail Sign In
gmail_sender = 'sender@gmail.com'
gmail_passwd = 'password'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
