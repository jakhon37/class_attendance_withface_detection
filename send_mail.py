# Import the following module
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import smtplib
import os

print('starting email sending function ...')
def initilaze_connection(m_mail, m_password):
    
    # initialize connection to our
    # email server, we will use gmail here
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    # Login with your email and password
    smtp.login(m_mail, m_password)


# send our email message 'msg' to our boss
def message(subject="Attendance Notification", text="", img=None, attachment=None):
    msg = MIMEMultipart()	# Add Subject
    msg['Subject'] = subject  
    msg.attach(MIMEText(text))
    msg['From'] = formataddr(('Class Attendance', 'jakhon@gachon.ac.kr'))

    return msg



def main_mail(m_mail, m_password, mail_to_send, attn_info):
    # initialize connection to our
    # email server, we will use gmail here
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    # Login with your email and password
    smtp.login(m_mail, m_password)

    # Call the message function
    text_send = f"Your attendance has been recorded! \nAttendance details: \n{attn_info}"
    msg = message("Attendance Notification", text_send)
               # r"C:\Users\Dell\Downloads\Garbage\Cartoon.jpg",
               # r"C:\Users\Dell\Desktop\slack.py")

    # Make a list of emails, where you wanna send mail
    to = mail_to_send #["ABC@gmail.com", "XYZ@gmail.com", "insaaf@gmail.com"]
    # sender_name = 'gachonn'
    # m_mail = {m_mail:sender_name}
    # Provide some data to the sendmail function!
    smtp.sendmail(m_mail, # "hello@gmail.com"
                to, msg.as_string())

    # Finally, don't forget to close the connection
    smtp.quit()
if __name__ == "__main__":
    m_mail, m_password, mail_to_send = 'bestuzbtube@gmail.com', '959707uzb', 'jakhon37@gmail.com'
    m_mail, m_password, mail_to_send, attn_info = 'jakhon@gachon.ac.kr', '#a123123', 'jakhon37@gmail.com', '1-11-2022   17:42:35'
    main_mail(m_mail, m_password, mail_to_send, attn_info)
    print('email sending is done...')