import os
def find_files(filename, search_path):
   result = []
# Wlaking top-down from the root
   for root, subdirs, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

path=find_files("test","/Users/anandswaroop/")
print(path)