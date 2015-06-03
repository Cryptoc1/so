# So, a plain English CLI for your favourite movies and shows
import requests, sys

query = '%20'.join(sys.argv[1:])
request = "http://www.omdbapi.com/?t={}".format(query)

r = requests.get(request)

if r.status_code == 200:
	if r.json()['Error']:
		english_query = query.replace('%20', ' ')
		print "Error: {}".format(r.json()['Error'])
	else:
		print r.json()

else:
	print 'Error: Request was not made'
