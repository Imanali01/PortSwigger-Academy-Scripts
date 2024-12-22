## Password reset poisoning via middleware
### Lab Scenario
This lab is vulnerable to password reset poisoning. The user `carlos` will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account. You can log in to your own account using the following credentials: `wiener:peter`. Any emails sent to this account can be read via the email client on the exploit server.

### Instructions
To solve this lab using the script:
1. Access the lab here: `https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-poisoning-via-middleware`
2. Run `python3 script.py <your lab URL>`