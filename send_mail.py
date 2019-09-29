import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '03187096fa1894'
    password = 'e3702a028d875b'
    message = f"<h3>Novo envio de feedback</h3><ul><li>Cliente: {customer}</li><li>Atendente: {dealer}</li><li>Avaliação: {rating}</li><li>Comentários: {comments}</li></ul>"
    sender_email = 'zanlucathiago@gmail.com'
    receiver_email = 'zanlucathiago@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feedback da Joacida'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())