#!/usr/bin/python
"""Handle uploading of a file to the server.

It only accepts files whose filename looks like an MD5 checksum.
"""
import cgi, cgitb
import sys
cgitb.enable(display=0, logdir=sys.environ["UPLOAD_LOG_DIR"])

form = cgi.FieldStorage()
filedata = form['files[]']

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print str(filedata)
