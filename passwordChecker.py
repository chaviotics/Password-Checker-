import requests # allows us to have a browser 

url = 'https://api.pwnedpasswords.com/range/' + 'password123'
res = requests.get(url)

print(res)