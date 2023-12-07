import datetime as dt
import smtplib
import random

my_email = "thapa.ramesh474@gmail.com"
password = "mlsg edyp mfhu rjen"

placeholder = "[NAME]"
now = dt.datetime.now()

with open("/Python 100 days challenge/Day 29 (smtp Email)/birthdays.csv") as file:
    next(file)
    data = file.read().splitlines()
    for line in data:
        name, email, year, month, day = line.split(",")
        birthday = dt.datetime(int(year), int(month), int(day))

        if birthday.date() == now.date():
            person_birthday = name
            file_path = f"/Python 100 days challenge/Day 29 (smtp Email)/letter_{random.randint(1,3)}.txt"
            with open(file_path) as letter:
                letter_to_exhange = letter.read()
                letter_to_exhange = letter_to_exhange.replace(placeholder, name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:Happy Birthday\n\n{letter_to_exhange}",
                )
                print(f"Email sent to {email}")
                connection.close()
        else:
            print("No birthday today")
            break
