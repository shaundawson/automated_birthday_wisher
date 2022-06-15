from config import password, my_email
import datetime as dt
import pandas as pd
import random
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
          letter_contents = letter_file.read()
          new_letter = letter_contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        # connection.starttls()
        connection.ehlo()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{new_letter}"
        )