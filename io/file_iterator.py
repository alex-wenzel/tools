"""
Defines a function to iterate one line at a time over files.  Useful
for large files
"""

#Global

#Local

def iterate(tsvfile, headers=False):
    """yields one line of a file at a time"""
    tsvline = tsvfile.readline()
    while tsvline != '':
        if headers:
            headers = False
            continue
        yield tsvline
        tsvline = tsvfile.readline()

