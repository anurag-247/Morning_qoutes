import smtplib
import datetime as dt
import random

my_email = "captainrogers3069@gmail.com"
password = "**************"

with open("quotes.txt", "r") as f:
    data = f.readlines()
# print(data)
q = random.choice(data)
# print(q)
now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

if day_of_week == 2:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="tonystark3069@yahoo.com", msg=f'Subject:Hello\n\n{q}')
        connection.close()


# print(day_of_week)

# dob = dt.datetime(year=2001, month=1, day=1)
# print(dob)


