from sys import argv
from os.path import exists

script, from_file_path, to_file_path = argv

# shortest version

open(to_file, 'w').write(open(from_file).read())
