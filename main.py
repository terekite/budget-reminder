import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 1. Read Data
import pandas as pd
#https://docs.google.com/spreadsheets/d//edit?usp=sharing&ouid=114941274988909858330&rtpof=true&sd=true
SHEET_ID = '19OXdN8kHxVJM_owhLUSOnsihDc7EOb-4'
SHEET_NAME = 'Mar_2024'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
data = df.loc[0]
money_left = data['LEFT TO SPEND:']


# 2. Send email
# message = MIMEMultipart()
# message["To"] = 'Omar & Kristine'
# message["From"] = 'Winter'
# message["Subject"] = 'Hello! Your Budget Reminder for the Day'

# title = '<b> Title line here. </b>'
# messageText = MIMEText(f'''You have {money_left} remaining for this month.''','html')
# message.attach(messageText)

# email = 'omarmahmoud2552@gmail.com'
# password = 'vknm omya vzje mhry'

# server = smtplib.SMTP('smtp.gmail.com:587')
# server.ehlo('Gmail')
# server.starttls()
# server.login(email,password)
# fromaddr = 'omarmahmoud2552@gmail.com'
# toaddrs  = 'omar.mail@icloud.com'
# server.sendmail(fromaddr,toaddrs,message.as_string())
#toaddrs  = 'kristinetangg@gmail.com'
#server.sendmail(fromaddr,toaddrs,message.as_string())

# server.quit()

