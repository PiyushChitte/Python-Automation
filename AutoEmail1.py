# create and send simple text message through Email


import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("pczone.devlops@gmailcom", "Piyush@1102")

message = "Email through Python Automation"

s.sendemail("pczone.devlops@gmail.com", "piyush.chitte2020@gmail.com", message)

s.quit()