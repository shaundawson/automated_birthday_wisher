import smtplib
from config import password, my_email

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.ehlo()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="iamsdawson@gmail.com", 
        msg="Subject:Hello\n\n This is the body of my email."
    )


