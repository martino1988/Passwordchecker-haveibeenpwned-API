import requests
import hashlib


# api-endpoint
def get_hashes(password_to_check):
    # get sha1-hash of password
    encoded_str = password_to_check.encode()
    hash_obj = hashlib.sha1(encoded_str)
    hexa_value = hash_obj.hexdigest()

    # get first digits of hash
    first5 = hexa_value[:5]
    hash = hexa_value[5:]

    # sending get request and saving the response as response object
    URL = "https://api.pwnedpasswords.com/range/{0}".format(first5)
    r = requests.get(url=URL)

    # format response
    password_hashes = r.text.split()

    # split every line in hash and breach-count
    hashlist = []
    for f in password_hashes:
        hashlist.append(f.split(":", 1))

    return_hash = 0
    for h in hashlist:
        if h[0] == hash.upper():
            # get the databreach-count
            return_hash = int(h[1])
            break
    return return_hash

