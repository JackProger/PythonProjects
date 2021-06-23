import smtplib as root
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
    login = input('Введите вашу почту: ')
    password = input('Введите ваш пароль от почты: ')
    url = 'smtp.mail.ru'
    toaddr = input('Кому: ')
    topic = input('Тема: ')
    message = input('Введите сообщение: ')
    num = int(input('Количество писем: '))
    for value in range( num ):
            msg = MIMEMultipart()
            msg['Subject'] = topic
            msg['From'] = login
            body = message

            msg.attach(MIMEText(body, 'plain'))
    
 
            server = root.SMTP_SSL(url, 465)
            server.login(login, password)
            server.sendmail(login, toaddr, msg.as_string())
            value += 1
            print(f'Отправлено {value}') 
            

def main():
    send_mail()

if __name__ == '__main__':
    main()
