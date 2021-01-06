import os
import shutil

MAIN = r'/Users/anandswaroop/Documents/C3/G6CA-Images'

DIRS = r'/Users/anandswaroop/Documents/C3/G6CA-yuarykes'

for root, subdirs, files in os.walk(DIRS):
    print('root', root)
    print('subdirs', subdirs)
    print('files', files)
    for file in files:
        path = os.path.join(root, file)
        shutil.copy(path, MAIN)
