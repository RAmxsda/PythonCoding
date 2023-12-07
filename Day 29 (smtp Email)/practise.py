# import smtplib

# my_email = "thapa.ramesh474@gmail.com"
# password = "mlsg edyp mfhu rjen"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="thapa.ramesh474@outlook.com",
#     msg="Subject:Hello\n\nThis is a test email from Senior Software Developer Ramesh Bahadur Thapa",
# )

# connection.close()

import datetime as dt


now = dt.datetime.now()

print(now.year)

print(now.month)

print(now.day)

print(now.hour)
print(now.weekday())

date_of_birth = dt.datetime(year=2000, month=1, day=1)

print(date_of_birth)

print(now - date_of_birth)

# to calculate how old are you
calculate_age = now.year - date_of_birth.year
print(f"You are {calculate_age} years old")
