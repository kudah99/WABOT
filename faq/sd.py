import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('albanelservices@gmail.com','oewdsplzastsnxud')
print("sending....")
server.sendmail('albanelservices@gmail.com','musekiwamasimbaashe@gmail.com','kkkkk')
print("send")