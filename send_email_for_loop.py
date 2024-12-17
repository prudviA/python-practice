import smtplib
import datetime

Gmail_id="prudhviachuth77299@gmail.com"
Gmail_password="ajwz yupv dodk ussj"

def send_email(to,subject,message):

    #creating a bridge to send a email

    for i in to:
        msg=smtplib.SMTP('smtp.gmail.com',587)
        msg.starttls()
        msg.login(Gmail_id,Gmail_password)
        #structure of email
        msg.sendmail(Gmail_id,to,f"Subject:{subject}\n\n{message}")
        
        msg.quit() #we are just breaking the bridge

#it help us to determine if a script is a main program or we are going to use 
if __name__=="__main__":
    recipient_email=["prudviathava@gmail.com","ahmadunishasyed@gmail.com"]
    subject="Happy Birthday!! :)"
    message="wishing you a good one <3"

    send_email(recipient_email,subject,message)