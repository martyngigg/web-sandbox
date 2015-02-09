#!/usr/bin/python
"""Handle uploading of a file to the server.

"""
import cgi
import os

UPLOAD_DIR = os.environ["MANTID_MD5_DATA_STORE"]

def save_uploaded_file (file_item, upload_dir):
    if not file_item.file:
        raise ValueError("File item has not file attribute")
    fout = file (os.path.join(upload_dir, file_item.filename), 'wb')
    while 1:
        chunk = file_item.file.read(100000)
        if not chunk:
            break
        fout.write (chunk)
    fout.close()

#------------------------------------------------------

try:
    form = cgi.FieldStorage()
    file_items = form['files[]']
except KeyError:
    location = "http://localhost/no_files_attrib_error.html"
    headers = "Content-type: text/html"
    body = "<p>Form does contain a 'files[]' field<p>"
else:
    # You only get a list back if you're uploading multiple files.
    # Make sure we're always working with a list.
    if type(file_items) != type([]):
        file_items = [file_items]

    errors = ""
    for file_item in file_items:
        try:
            save_uploaded_file(file_item, UPLOAD_DIR)
        except Exception, exc:
            errors += "<p>Failed to upload %s</p>\n" % (file_item.filename)
    #endfor
    if errors == "":
        location = "http://localhost/success.html"
        headers = "Content-type: text/html\n"\
                  "Status: 303 see other\n"\
                  "Location: %s" % location
        body = ""
    else:
        headers = "Content-type: text/html"
        body = errors

# ------ Output -------
print headers
print
print body


