# Web Security Academy Scripts
This repository contains Python scripts I developed to solve various labs from PortSwigger's Web Security Academy. These scripts automate the process of exploiting the vulnerabilities found in the academy's labs. 

## Table of Contents
<details>
  <summary>SQL Injection</summary>

  - [SQL injection vulnerability allowing login bypass](./SQL%20Injection%20Labs%2FSQL%20injection%20vulnerability%20allowing%20login%20bypass)
  - [SQL injection attack, querying the database type and version on Oracle](./SQL%20Injection%20Labs/SQL%20injection%20attack,%20querying%20the%20database%20type%20and%20version%20on%20Oracle)
  - [SQL injection attack, querying the database type and version on MySQL and Microsoft](./SQL%20Injection%20Labs%2FSQL%20injection%20attack%2C%20querying%20the%20database%20type%20and%20version%20on%20MySQL%20and%20Microsoft)
  - [SQL injection attack, listing the database contents on non-Oracle databases](./SQL%20Injection%20Labs/SQL%20injection%20attack,%20listing%20the%20database%20contents%20on%20non-Oracle%20databases)
  - [SQL injection attack, listing the database contents on Oracle](./SQL%20Injection%20Labs/SQL%20injection%20attack,%20listing%20the%20database%20contents%20on%20Oracle)
  - [Blind SQL injection with conditional responses](./SQL%20Injection%20Labs/Blind%20SQL%20Injection%20with%20Conditional%20Responses)
  - [Blind SQL injection with conditional errors](./SQL%20Injection%20Labs/Blind%20SQL%20injection%20with%20conditional%20errors)
  - [Visible error-based SQL injection](./SQL%20Injection%20Labs%2FVisible%20error-based%20SQL%20injection)
  - [Blind SQL injection with time delays](./SQL%20Injection%20Labs/Blind%20SQL%20injection%20with%20time%20delays)
  - [Blind SQL injection with time delays and information retrieval](./SQL%20Injection%20Labs/Blind%20SQLi%20with%20time%20delays%20and%20informational%20retrieval)
</details>

<details>
  <summary>XXE Injection</summary>

  - [Exploiting XXE using external entities to retrieve files](./XXE%20Injection%2FExploiting%20XXE%20using%20external%20entities%20to%20retrieve%20files)
  - [Exploiting XXE to perform SSRF attacks](./XXE%20Injection%2FExploiting%20XXE%20to%20perform%20SSRF%20attacks)
  - [Exploiting XInclude to retrieve files](./XXE%20Injection/Exploiting%20XInclude%20to%20retrieve%20files)
  - [Exploiting XXE via image file upload](./XXE%20Injection/Exploiting%20XXE%20via%20image%20file%20upload)

</details>

<details>
  <summary>Server-Side Request Forgery (SSRF)</summary>

  - [Basic SSRF against the local server](./SSRF/Basic%20SSRF%20against%20the%20local%20server)
  - [Basic SSRF against another back-end system](./SSRF/Basic%20SSRF%20against%20another%20back-end%20system)
  - [SSRF with blacklist-based input filter](./SSRF/SSRF%20with%20blacklist-based%20input%20filter)
  - [SSRF with filter bypass via open redirection vulnerability](./SSRF/SSRF%20with%20filter%20bypass%20via%20open%20redirection)
  - [SSRF with whitelist-based input filter](./SSRF/SSRF%20with%20whitelist-based%20input%20filter)

</details>

<details>
  <summary>Command Injection</summary>

  - [OS command injection, simple case](./Command%20Injection/OS%20command%20injection,%20simple%20case)
  - [Blind OS command injection with time delays](./Command%20Injection/Blind%20OS%20command%20injection%20with%20time%20delays)
  - [Blind OS command injection with output redirection](./Command%20Injection/Blind%20OS%20command%20injection%20with%20output%20redirection)

</details>

<details>
  <summary>Path Traversal</summary>

  - [File path traversal, simple case](./Path%20Traversal/File%20path%20traversal,%20simple%20case)
  - [File path traversal, traversal sequences blocked with absolute path bypass](./Path%20Traversal/File%20path%20traversal,%20traversal%20sequences%20blocked%20with%20absolute%20path%20bypass)
  - [File path traversal, traversal sequences stripped non-recursively](./Path%20Traversal/File%20path%20traversal,%20traversal%20sequences%20stripped%20non-recursively)
  - [File path traversal, traversal sequences stripped with superfluous URL-decode](./Path%20Traversal/File%20path%20traversal,%20traversal%20sequences%20stripped%20with%20superfluous%20URL-decode)
  - [File path traversal, validation of start of path](./Path%20Traversal/File%20path%20traversal,%20validation%20of%20start%20of%20path)
  - [File path traversal, validation of file extension with null byte bypass](./Path%20Traversal/File%20path%20traversal,%20validation%20of%20file%20extension%20with%20null%20byte%20bypass)

</details>

<details>
  <summary>Web Cache Poisoning</summary>

  - [Web cache poisoning with an unkeyed header](./Web%20Cache%20Poisoning/Web%20cache%20poisoning%20with%20an%20unkeyed%20header)
  - [Web cache poisoning with an unkeyed cookie](./Web%20Cache%20Poisoning/Web%20cache%20poisoning%20with%20an%20unkeyed%20cookie)
  - [Web cache poisoning with multiple headers](./Web%20Cache%20Poisoning/Web%20cache%20poisoning%20with%20multiple%20headers)
  - [Targeted web cache poisoning using an unknown header](./Web%20Cache%20Poisoning/Targeted%20web%20cache%20poisoning%20using%20an%20unknown%20header)
  - [Web cache poisoning via an unkeyed query string](./Web%20Cache%20Poisoning/Web%20cache%20poisoning%20via%20an%20unkeyed%20query%20string)
  - [Web cache poisoning via an unkeyed query parameter](./Web%20Cache%20Poisoning/Web%20cache%20poisoning%20via%20an%20unkeyed%20query%20parameter)
  - [Parameter cloaking](./Web%20Cache%20Poisoning/Parameter%20cloaking)
  - [Web cache poisoning via a fat GET request](./Web%20Cache%20Poisoning/Web%20cache%20poisoning%20via%20a%20fat%20GET%20request)

</details>

<details>
<summary>Business Logic Vulnerabilities</summary>

- [Excessive trust in client-side controls](./Business%20Logic%20Vulnerabilities/Excessive%20trust%20in%20client-side%20controls)
- [High-level logic vulnerability](./Business%20Logic%20Vulnerabilities/High-level%20logic%20vulnerability)
- [Inconsistent security controls](./Business%20Logic%20Vulnerabilities/Inconsistent%20security%20controls)
- [Flawed enforcement of business rules](./Business%20Logic%20Vulnerabilities/Flawed%20enforcement%20of%20business%20rules)
- [Inconsistent handling of exceptional input](./Business%20Logic%20Vulnerabilities/Inconsistent%20handling%20of%20exceptional%20input)
- [Weak isolation on dual-use endpoint](./Business%20Logic%20Vulnerabilities/Weak%20isolation%20on%20dual-use%20endpoint)
- [Insufficient workflow validation](./Business%20Logic%20Vulnerabilities/Insufficient%20workflow%20validation)
- [Authentication bypass via flawed state machine](./Business%20Logic%20Vulnerabilities/Authentication%20bypass%20via%20flawed%20state%20machine)
- [Infinite Money Flaw](./Business%20Logic%20Vulnerabilities/Infinite%20money%20logic%20flaw)

</details>

<details>
<summary>HTTP Host header attacks</summary>

- [Basic password reset poisoning](./HTTP%20Host%20header%20attacks/Basic%20password%20reset%20poisoning)
- [Host header authentication bypass](./HTTP%20Host%20header%20attacks/Host%20header%20authentication%20bypass)

</details>


<details>
  <summary>File Upload</summary>

  - [Remote code execution via web shell upload](./File-Upload/Remote%20code%20execution%20via%20web%20shell%20upload)
  - [Web shell upload via Content-Type restriction bypass](./File-Upload%2FWeb%20shell%20upload%20via%20Content-Type%20restriction%20bypass)
  - [Web shell upload via path traversal](./File-Upload/Web%20shell%20upload%20via%20path%20traversal)
  - [Web shell upload via extension blacklist bypass](./File-Upload%2FWeb%20shell%20upload%20via%20extension%20blacklist%20bypass)
  - [Web shell upload via obfuscated file extension](./File-Upload/Web%20shell%20upload%20via%20obfuscated%20file%20extension)
</details>

<details>
  <summary>Access Control Vulnerabilities</summary>

  - [Unprotected admin functionality](./Access%20Control%20Vulnerabilities/Unprotected%20admin%20functionality)
  - [Unprotected admin functionality with unpredictable URL](./Access%20Control%20Vulnerabilities/Unprotected%20admin%20functionality%20with%20unpredictable%20URL)
  - [User role controlled by request parameter](./Access%20Control%20Vulnerabilities/User%20role%20controlled%20by%20request%20parameter)
  - [User role can be modified in user profile](./Access%20Control%20Vulnerabilities/User%20role%20can%20be%20modified%20in%20user%20profile)
  - [User ID controlled by request parameter](./Access%20Control%20Vulnerabilities/User%20ID%20controlled%20by%20request%20parameter)
  - [User ID controlled by request parameter, with unpredictable user IDs](./Access%20Control%20Vulnerabilities/User%20ID%20controlled%20by%20request%20parameter,%20with%20unpredictable%20user%20IDs)
  - [User ID controlled by request parameter with data leakage in redirect](./Access%20Control%20Vulnerabilities/User%20ID%20controlled%20by%20request%20parameter%20with%20data%20leakage%20in%20redirect)
  - [User ID controlled by request parameter with password disclosure](./Access%20Control%20Vulnerabilities/User%20ID%20controlled%20by%20request%20parameter%20with%20password%20disclosure)
  - [Insecure direct object references](./Access%20Control%20Vulnerabilities/Insecure%20direct%20object%20references)
  - [URL-based access control can be circumvented](./Access%20Control%20Vulnerabilities/URL-based%20access%20control%20can%20be%20circumvented)
  - [Method-based access control can be circumvented](./Access%20Control%20Vulnerabilities/Method-based%20access%20control%20can%20be%20circumvented)
  - [Multi-step process with no access control on one step](./Access%20Control%20Vulnerabilities/Multi-step%20process%20with%20no%20access%20control%20on%20one%20step)
  - [Referer-based access control](./Access%20Control%20Vulnerabilities/Referer-based%20access%20control)

</details>

<details>
  <summary>Authentication Vulnerabilities</summary>

  - [Username enumeration via different responses](./Authentication%20Vulnerabilities/Username%20enumeration%20via%20different%20responses)
  - [2FA simple bypass](./Authentication%20Vulnerabilities/2FA%20simple%20bypass)
  - [Password reset broken logic](./Authentication%20Vulnerabilities/Password%20reset%20broken%20logic)
  - [Username enumeration via response timing](./Authentication%20Vulnerabilities/Username%20enumeration%20via%20subtly%20different%20responses)
  - [Broken brute-force protection, IP block](./Authentication%20Vulnerabilities/Broken%20brute-force%20protection,%20IP%20block)
  - [Username enumeration via account lock](./Authentication%20Vulnerabilities/Username%20enumeration%20via%20account%20lock)
  - [Brute-forcing a stay-logged-in cookie](./Authentication%20Vulnerabilities/Brute-forcing%20a%20stay-logged-in%20cookie)
  - [Password reset poisoning via middleware](./Authentication%20Vulnerabilities/Password%20reset%20poisoning%20via%20middleware)

</details>
