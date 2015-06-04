#!/usr/bin/env python

# So, a plain English CLI for your favourite movies and shows
import requests, sys

DEVMODE = True
_usage = "Usage:\n\t./so.py <movie title>"

def main():
    # Make sure the user supplied some arguments
    if len(sys.argv) > 1:
        do_request(sys.argv)
    else:
        print _usage

def do_request(args):
    # Make our request
    request = "http://www.omdbapi.com/?t={}".format('%20'.join(args[1:]))
    r = requests.get(request)
    # Did the request fail?
    if r.status_code == 200:
        # Nope, it didn't
        resp = r.json()
        # Wait, we actually got stuff, RIGHT?!?!
        if resp['Response'] != "True":
            if DEVMODE:
                print 'Response not okay\n'
	    print r.json()['Error']
        # Phew, response returned some data
        else:
            if DEVMODE:
                print 'Response Okay\n'
            for i in resp:
                print format_resp(resp, i)
    else:
        # fuck, it did! :,(
        print 'Error: Request was not made'

# Make the data pertty
def format_resp(list, index):
    return index + ": " + list[index]

# Enter the Matrix...
if __name__ == "__main__":
    main()
