import smtplib

class pytexting:
  def __init__(self, email, password):
    self.email = email
    self.password = password
    self.smtp = smtplib.SMTP("smtp.gmail.com:587")
    self.smtp.starttls()
    self.smtp.login(email, password)
    self.carriers = {

    "ATT":"@txt.att.net",
   "Sprint":"@messaging.sprintpcs.com",
   "T-Mobile":"@tmomail.net", 
   "Verizon":"@vtext.com",
   "Virgin":"@vmobl.com",
}

  def send(self, phone_num, message)
    