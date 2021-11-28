from haveibeenpwned import HaveIBeenPwned
from firefoxmonitor import FireFoxMonitor

websites_instances = [
    HaveIBeenPwned(), FireFoxMonitor()

]


def process_email(emails):
    for website in websites_instances:
        for email in emails:
            print(website.is_pwned(email))
