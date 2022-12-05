# Passwordchecker- using the haveibeenpwned-API

A sha1 hash of the password is generated and the first 5 digits from the hash are sent to the API of haveibeenpwned. 

All hashes starting with these 5 digits are received to check if the given password is among the already known data-breaches.

You can include this code in your web application to allow users to use only strong passwords.

### Live demonstrator:

https://pwdchecker.pythonanywhere.com/

### Installation

<pre><code> git clone https://github.com/martino1988/PwdChecker-haveibeenpwned-API.git </code></pre>

<pre><code> pip install -r requirements.txt </code></pre>

