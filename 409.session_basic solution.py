import requests

client = requests.Session()
client.cookies['sessionid'] = 'c66d499b490ba92536e3aa420125163c366cb00d683632bfb2a9e3f77061aa0a'
res = client.get("http://host3.dreamhack.games:23771/")
print(res.text)