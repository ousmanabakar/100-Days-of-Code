import random
import smtplib
import datetime as dt
with open("quotes.txt") as data:
    quote = data.read()
    list_of_quotes = quote.split("\n")

    now = dt.datetime.now()
    day_of_week = now.weekday()
    message = random.choice(list_of_quotes)

    if day_of_week == 6:
        my_email = "sender_email@gmail.com"
        password = "email_password"

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                from_addr=my_email,
                to_addrs="recipt_email@gmail.com",
                msg=f"Subject:Day Quote\n\n{message}."
                )
        print("email is successfully sent")

#
# def send_email():
#     my_email = "sender_email@gmail.com"
#     password = "email_password"
#
#     connection = smtplib.SMTP("smtp.gmail.com", port=587)
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="recip_email@gmail.com",
#         msg=f"Subject:Hello\n\n{random.choice(list_of_quotes)}."
#         )
#     connection.close()




# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# data_of_birthday = dt.datetime(year=1960, month=8, day=11)
# print(data_of_birthday)
