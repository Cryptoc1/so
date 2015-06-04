# So, a plain English CLI for your favourite movies and shows
import requests, sys

query = '%20'.join(sys.argv[1:])
request = "http://www.omdbapi.com/?t={}".format(query)

r = requests.get(request)

print r.status_code

if r.status_code == 200:
	if r.json()['Response']:
		print 'response fine'
		print r.json()['Plot']
	else:
		print 'response not ok'
		print r.json()['Error']
else:
	print 'Error: Request was not made'