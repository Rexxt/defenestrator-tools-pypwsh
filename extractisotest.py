import iso
from distutils.dir_util import copy_tree
from sys import argv, exit
args = argv[1:]

if len(args) != 2:
    print('need 2 args (ISO, destination)')
    exit(127)

info = iso.mount(args[0])
wrapper = iso.ISOInfoWrapper(info)
from_directory = f'{wrapper.drive_letter}:\\'
to_directory = args[1]
copy_tree(from_directory, to_directory)
wrapper.dismount()
