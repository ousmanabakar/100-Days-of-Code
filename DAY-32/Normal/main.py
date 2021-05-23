import datetime as dt
import random
import smtplib
import pandas
My_mail = "your_email1@gmail.com"
PASSWORD = "your_password"
now = dt.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_data:
        letter = letter_data.read()
        letter = letter.replace("[NAME]", birthdays_person["name"])
        print(letter)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(My_mail, PASSWORD)
        connection.sendmail(
            from_addr=My_mail,
            to_addrs=birthdays_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )
