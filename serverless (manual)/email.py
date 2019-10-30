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

# change DAY1 to corresponding day list
with open('collegeDAY1.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)

# loop
for i in range(451):
        try:
                college = obj[i]['College']
                email = obj[i]['Email']
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login(emailAddress, emailPassword)
                body = "Hi " + college + ",\n\n" + "YOUR MESSAGE HERE"
                message = 'Subject: {}\n\n{}'.format("College Interest", body)
                server.sendmail(
                        emailAddress, 
                        email, 
                        message)
                server.quit()
                print("email " + str(i+1) + "/451 sent (" + college + ")")
        
        except:
                print("exception: runtime error")
                break
