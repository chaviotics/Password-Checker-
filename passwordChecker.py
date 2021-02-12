import requests # allows us to have a browser # we use the api of pwnedpasswords.
import hashlib # lets us import the SHA1

# url = 'https://api.pwnedpasswords.com/range/' + '20177' # uses SHA1 Algo from 20177DAFA4C488828B70993C896D5ECA7A38C9C2
# res = requests.get(url)

# print(res) # <Response [400]> -> Unauthorized, something's wrong with the api; we want [200]

# key anonymity - technique used alot

def requests_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching {res.status_code}, check api and try again.") 
    return res

def pwned_api_check(password): # checks the password if it exists in API response
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

# requests_api_data('123')
pwned_api_check('123')