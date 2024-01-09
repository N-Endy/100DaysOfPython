import smtplib

# my_email = "okafornel@gmail.com"
# password = "abcd1234()"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Layer security, prevents email from being read with encryption if intercepted
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="example.gmail.com", msg="Subject:Hello\n\nThis is the body of the email")

import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)

date_of_birth = dt.datetime(year=1990, month=11, day=26)
print(date_of_birth)