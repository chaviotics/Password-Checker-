import requests # allows us to have a browser # we use the api of pwnedpasswords.
import hashlib # lets us import the SHA1
import sys

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

def get_password_leaks_count(hashes, hash_to_check): # hash_to_check is our password tail to be checked
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # print(hashes)
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password): # checks the password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = requests_api_data(first5_char)
    # print(sha1password)
    # print(first5_char, tail)
    # print(response)
    return get_password_leaks_count(response, tail)

# requests_api_data('123')
# pwned_api_check('123')

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. You should change your password.')
        else:
            print(f"{password} was NOT found. Good password! Carry on!")
    return "All done!"


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# sys.exit exits the file and returns the value of the function

# Tips to make this better:
# Maybe read these passwords instead of the command line because the command line stores the previous commands.