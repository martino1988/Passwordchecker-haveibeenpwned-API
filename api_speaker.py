import requests


# api-endpoint
def get_hashes(digits, hash):
  URL = "https://api.pwnedpasswords.com/range/{0}".format(digits)
     
  # defining a params dict for the parameters to be sent to the API
  
  # sending get request and saving the response as response object
  r = requests.get(url = URL)
  
  password_hashes = r.text.split()
  hashlist = []
  
  for f in password_hashes:
    hashlist.append(f.split(":", 1))

  return_hash = ""
  for h in hashlist:
    if h[0] == hash.upper():
      return_hash = h[1]
      break
  return return_hash