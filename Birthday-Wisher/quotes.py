import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

MY_EMAIL = "okafornel@gmail.com"
MY_PASSWORD = "anypassword"
destination = ""

if weekday == 1:
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=destination, msg=f"Subject:Motivation\n\n{quote}")