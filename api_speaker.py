import requests


# api-endpoint
def get_hashes(password_to_check):
  
  URL = "https://api.pwnedpasswords.com/range/{0}".format(digits)
   
  # get sha1-hash of password
  encoded_str = password_to_check.encode()
  hash_obj = hashlib.sha1(encoded_str)
  hexa_value = hash_obj.hexdigest()
  
  # get first digits of hash
  first5 = hexa_value[:5]
  last = hexa_value[5:]
  
  # sending get request and saving the response as response object
  r = requests.get(url = URL)
  
  # format response
  password_hashes = r.text.split()
  
  # split every line in hash and breach-count
  hashlist = []
  for f in password_hashes:
    hashlist.append(f.split(":", 1))

  return_hash = "0"
  for h in hashlist:
    if h[0] == hash.upper():
      return_hash = h[1]
      break
  return return_hash
