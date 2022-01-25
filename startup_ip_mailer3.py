#This script send an email to me at every boot up
#allows us to know the IP of each Pi without a monitor

import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import os

print('Now emailing IP to Bowieengineering')
uptime = 0
while uptime < 2:
    uptime = os.popen('uptime -p').read()[:-1]
    uptime = uptime.split(" ")
    uptime = int(uptime[1])


print("Working... Uptime is ", uptime)
# Change to your own account information
to = '*****************'
gmail_user = '************'
gmail_password = '**************'
#smtpserver = smtplib.SMTP('smtp.gmail.com', 587) #prev 587, 465
smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465) #prev 587, 465
smtpserver.ehlo()
#smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
print('still working')
# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
print(split_data[17])
ipaddr = split_data[17]
my_ip = 'The ip address for Pi6 is %s' %  ipaddr
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi6 on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
print(msg)
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
#quit()
print("All Done")
