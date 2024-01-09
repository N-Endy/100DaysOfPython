import smtplib
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    