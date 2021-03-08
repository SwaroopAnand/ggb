import os
import shutil


def ExtractImages (GGBFile, ReplaceImages):

    for root, subdir, files in os.walk(GGBFile):
        print('root', root)
        print('subdir', subdir)
        print('files', files)
        for file in files:
            path = os.path.join(root, file)
            shutil.move(path, ReplaceImages)

ExtractImages('/Users/anandswaroop/Documents/ReplaceTest/Demo/GGBFiles/QA_material-pdyusxf6', '/Users/anandswaroop/Documents/ReplaceTest/Demo/GGBFiles/UA_Assets_QA')