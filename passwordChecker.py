import requests # allows us to have a browser 
# we use the api of pwnedpasswords.com

url = 'https://api.pwnedpasswords.com/range/' + '20177' # uses SHA1 Algo from 20177DAFA4C488828B70993C896D5ECA7A38C9C2
res = requests.get(url)

print(res) # <Response [400]> -> Unauthorized, something's wrong with the api; we want [200]

# key anonymity - technique used alot

def requests_api_data(query_char):
    pass

def pwned_api_check(password):
    pass
