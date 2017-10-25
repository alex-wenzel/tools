"""
Two functions for reading text config files, one to read lines into a list
and one to read lines with an '=' character into key-value dictionaries
"""

#Global

#Local
import tools.io.file_iterator as file_iterator

def read_config(conf_path):
    """Reads a file of single strings on each line"""
    return [line.strip('\n') for line in open(conf_path).readlines() if line[0] != '#']

def read_config_kv(conf_path):
    """Reads a file of key value pairs separated by 1 '=', one on each line"""
    outd = {}
    for line in file_iterator.iterate(open(conf_path)):
        if line[0] != '#' and line != "\n":
            line = line.strip('\n')
            try:
                key, value = line.split('=')
                outd[key] = value
            except ValueError:
                raise ValueError("improperly formatted key=value pair")
    return outd
