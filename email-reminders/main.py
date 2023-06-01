# This program makes use of smtplib library to send emails
# to remind of relatives and family`s birthdays.
# SMTP - Simple Mail Transfer Protocol

import smtplib
import os
import datetime as dt
import pandas
from dotenv import load_dotenv, dotenv_values


data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient="records")
# Sample record: {'person': 'Alex', 'title': 'sister', 'birthday': '2023-9-7'}

now = dt.datetime.now()
today_day = now.day
today_month = now.month
datetime_format = '%Y-%m-%d' # matches the format in the records


def send_mail(name, relationship, birthday):

    load_dotenv()

    # Get stored info from .env file.
    sender_email = os.getenv('EMAIL')
    sender_password = os.getenv('PASSWORD')
    smtp_host = os.getenv('SMTP_HOST')
    receiver = os.getenv('RECEIVER')

    # Replace keywords from the content of the email with actual info on the person
    with open("email_contents.txt") as file:
        content = file.read()
        content = content.replace("[NAME]", name)
        content = content.replace("[RELATIONSHIP]", relationship)
        content = content.replace("[DATE]", birthday)

    # Log in to your account
    with smtplib.SMTP(host=smtp_host, port=587) as conn:
        conn.starttls()
        conn.login(user=sender_email, password=sender_password)
        conn.sendmail(
            from_addr=sender_email,
            to_addrs=receiver,
            msg=f"Subject: IT IS {name.title()}`s BIRTHDAY!!! \n\n{content}"
        )


for bday in birthdays_dict:
    # since bday['birthday'] is a string, need to convert it to date_obj
    birthday = bday['birthday']
    bday_obj = dt.datetime.strptime(birthday, datetime_format)
    if bday_obj.month == today_month and bday_obj.day == today_day:
        name = bday['name']
        relationship = bday['relationship']
        send_mail(name, relationship, birthday)
