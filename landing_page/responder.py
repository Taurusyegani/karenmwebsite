import smtplib

my_email = "taurus.pearson1@gmail.com"
password = "asaqnhjzsjrhruob"

class Responder:
     def __init__(self, email, phone, name, message):
          self.phone = phone
          self.email = email
          self.name = name
          self.message = message

     def send_email(name, email, phone, message):
         email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
         with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=my_email, password=password)
             connection.sendmail(
                 from_addr=my_email,
                 to_addrs="taurus.pearson@icloud.com",
                 msg=email_message
             )