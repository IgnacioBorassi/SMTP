from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
 
 
message = "Hola q onda"
 
password = ""
msg['From'] = "ignacioborassi@gmail.com"
msg['To'] = "iborassi@alumno.huergo.edu.ar"
msg['Subject'] = "pruebapruebaasd"
 
msg.attach(MIMEText(message, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
server.login(msg['From'], password)
 
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("successfully sent email")

