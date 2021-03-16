# SMTPAuthenticationError
   # To solve above error during execution of script follow below steps
   # Step 1: Ensure your password is correct
   # Step 2: Disabling CAPTCHA for clients - Login through your gmail and go to below link and enable the setting 
   # https://accounts.google.com/DisplayUnlockCaptcha
   # Step 3: Gmail blocks sign-in from apps which do not use modern security standards. You can however, turn on/off this safety feature by going to the link below:
   # https://www.google.com/settings/security/lesssecureapps  




import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls() 
# Authentication 
s.login("email-id", "password") 
# message to be sent 
message = "message sent using python"
# sending the mail 
s.sendmail("senders_email_id", "recievers_email_id", message) 
# terminating the session 
s.quit()

# __________________extended version 
gmail_user = "email-id"
gmail_pwd = "password"
TO = 'To-email-id'
SUBJECT = "Email using pyhton"
TEXT = "Hi there, Testing smtplib"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])

server.sendmail(gmail_user, [TO], BODY)
print ('email sent')

# ------------------------------------Scheduling
import datetime as dt
import time
def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    
    # Code given above is to be inserted here for performing send action

    print('email sent')

first_email_time = dt.datetime(2020,10,26,3,0,0) # set your sending time in UTC
interval = dt.timedelta(minutes=2*60) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval