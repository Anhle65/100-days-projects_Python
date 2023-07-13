import smtplib
import random


def list_wishes():
    with open("quotes.txt") as quotes:
        line = random.choice(quotes.readlines())
    return line


def send_mail(message):
    user_mail = "levananh2358@gmail.com"
    password = 'frpppenewofwdwbv'
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=user_mail, password=password)
    connection.sendmail(from_addr=user_mail, to_addrs="levananh235813@gmail.com", msg=f"Subject: New day-New quote\n\n{message}")
    connection.close()


def motivation():
    message = list_wishes()
    send_mail(message)

motivation()
