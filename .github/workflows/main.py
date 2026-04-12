import pandas
import smtplib
from datetime import datetime # import datetime class
import random
import os

PLACEHOLDER = "[NAME]"
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = datetime.now()
# current_day = today.day
# current_month = today.month
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
#birthdays_dict = data.to_dict(orient="records")
birthdays_dict = {(data_row.month, data_row.day) : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict: #check keys match
    birthday_person = birthdays_dict[today_tuple] # get row from dict
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'

    with open(file_path) as letter_file:
        letter_contents = letter_file.read()
        letter_contents = letter_contents.replace(PLACEHOLDER, birthday_person["name"])
        print(letter_contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:  # smtp.mail.yahoo.com
        connection.starttls()  # encrpt message
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
            msg=f'Subject:Happy Birthday!\n\n{letter_contents}')
