import smtplib

my_email = "okafornel@gmail.com"
password = "abcd1234()"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # Layer security, prevents email from being read with encryption if intercepted
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="example.gmail.com", msg="Subject:Hello\n\nThis is the body of the email")