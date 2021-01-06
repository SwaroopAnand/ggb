import os
import shutil

MAIN = r'/Users/anandswaroop/Documents/test/C6G6Pics'

DIRS = r'/Users/anandswaroop/Documents/test/material-eaknfkae'

for root, subdirs, files in os.walk(DIRS):
    print('root', root)
    print('subdirs', subdirs)
    print('files', files)
    for file in files:
        path = os.path.join(root, file)
        shutil.move(path, MAIN)
