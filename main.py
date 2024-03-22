import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
message = MIMEMultipart()
message["To"] = 'Omar Ali'
message["From"] = 'budget-reminder'
message["Subject"] = 'Hello! Your Budget Reminder for the Day'

title = '<b> Title line here. </b>'
messageText = MIMEText('''Message body goes here.''','html')
message.attach(messageText)

email = 'omarmahmoud2552@gmail.com'
password = 'vknm omya vzje mhry'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo('Gmail')
server.starttls()
server.login(email,password)
fromaddr = 'omarmahmoud2552@gmail.com'
toaddrs  = 'omar.mail@icloud.com'
server.sendmail(fromaddr,toaddrs,message.as_string())
#toaddrs  = 'kristinetangg@gmail.com'
#server.sendmail(fromaddr,toaddrs,message.as_string())

server.quit()

