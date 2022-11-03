import yagmail

def main_mail(m_mail, m_password, mail_to_send, attn_info):
    receiver = mail_to_send
    body = f"Hello there from Yagmail {attn_info}"
    sendr = "gaachon"
    m_mail = {m_mail:sendr}
    yag = yagmail.SMTP(m_mail, m_password)
    yag.send(
        to=receiver,
        subject="Yagmail test with attachment",
        contents=body#, 
       # attachments=filename,
    )


if __name__ == "__main__":
    m_mail, m_password, mail_to_send = 'bestuzbtube@gmail.com', '959707uzb', 'jakhon37@gmail.com'
    m_mail, m_password, mail_to_send, attn_info = 'jakhon@gachon.ac.kr', '#a123123', 'jakhon37@gmail.com', '1-11-2022   17:42:35'
    main_mail(m_mail, m_password, mail_to_send, attn_info)
    print('email sending is done...')