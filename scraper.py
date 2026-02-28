import requests
from bs4 import BeautifulSoup
import time


login_url = "https://the-internet.herokuapp.com/authenticate"
secure_url = "https://the-internet.herokuapp.com/secure"

payload = {"username": "tomsmith",
           "password": "SuperSecretPassword!"
           }

session = requests.Session()
response = session.post(login_url, data=payload)

retries = 3
for attempt in range(retries):
    try:
        response = session.get(secure_url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.select_one("h2").get_text(strip=True)
            massage = soup.select_one("h4.subheader").get_text(strip=True)
            print(title)
            print(massage)
            break

    except:
        print("Something went wrong", attempt + 1)
        time.sleep(2)
