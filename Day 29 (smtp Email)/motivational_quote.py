import smtplib
import datetime as dt
import random

my_email = "thapa.ramesh474@gmail.com"
password = "mlsg edyp mfhu rjen"

now = dt.datetime.now()

if now.weekday() == 1:
    with open(
        "/Python 100 days challenge/Day 29 (smtp Email)/quotes.txt"
    ) as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="thapa.ramesh474@outlook.com",
            msg=f"Subject:Tuesday Motivation\n\n{quote}",
        )

        connection.close()
