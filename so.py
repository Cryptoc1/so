#!/usr/bin/env python
# So, a plain English CLI for your favourite movies and shows
import requests, sys


DEVMODE = True
_usage = "Usage:\n\t./so.py <movie title>"

def main():
    if len(sys.argv) > 1:
        do_request(sys.argv)
    else:
        print _usage

def do_request(args):
    request = "http://www.omdbapi.com/?t={}".format('%20'.join(args[1:]))
    r = requests.get(request)
    # Make sure the request didn't fail
    if r.status_code == 200:
        resp = r.json()
        if resp['Response'] != "True":
            if DEVMODE:
                print 'Response not okay\n'
	    print r.json()['Error']
        else:
            if DEVMODE:
                print 'Response Okay\n'
            for i in resp:
                print format_resp(resp, i)
    else:
        print 'Error: Request was not made'

def format_resp(list, index):
    return index + ": " + list[index]

if __name__ == "__main__":
    main()
