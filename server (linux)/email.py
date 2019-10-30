import json
import smtplib
import subprocess
import time

# 1) make a new gmail account
# 2) set your account to allow less secure apps
# 3) https://www.google.com/settings/security/lesssecureapps

# 4) enter gmail credentials
emailAddress = "email@gmail.com"
emailPassword = "password123"

# read file
with open('colleges.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)

# loop
for i in range(1718):
        try:
                college = obj[i]['College']
                email = obj[i]['Email']
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login(emailAddress, emailPassword)
                body = "Hi " + college + ",\n\n" + "YOUR MESSAGE HERE"
                message = 'Subject: {}\n\n{}'.format("College Interest", body)
                server.sendmail(emailAddress, email, message)
                server.quit()
                print("email " + str(i+1) + "/1718 sent (" + college + ")")
                time.sleep(210)
        
        except:
                print("exception: runtime error")
                break
