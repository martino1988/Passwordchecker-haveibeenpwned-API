# Passwordchecker- using the haveibeenpwned-API

A sha1 hash of the password is generated and the first 5 digits from the hash are sent to the API of haveibeenpwned. 

All hashes starting with these 5 digits are received to check if the given password is among the already known data-breaches.

You can include this code in your web application to allow users to use only strong passwords.

### Live demonstrator:

https://pwdchecker.pythonanywhere.com/

### Installation

<pre><code>Tpip install -r requirements.txt</code></pre>

