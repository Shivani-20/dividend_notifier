import smtplib
import stocks
from plyer import notification
from dotenv import load_dotenv
import os

try:
    load_dotenv()
    dividends=stocks.getDividendDetails()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(os.getenv("SENDER"), os.getenv("PASSWD"))
    # message to be sent
    message = dividends
    # sending the mail
    s.sendmail(os.getenv("SENDER"), os.getenv("RECEIVER"), message)
    # terminating the session
    s.quit()
    notification.notify(title="", app_icon="dollar.ico", message="Upcoming dividends sent to email", timeout=10)
except:
    notification.notify(title="", app_icon="dollar.ico", message="Not able to send ex date of dividends", timeout=10) 
