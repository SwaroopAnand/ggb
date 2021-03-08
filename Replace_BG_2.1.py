import os
import shutil
import os
def find_files(filename, search_path):
   result = []
# Wlaking top-down from the root
   for root, subdirs, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result
path=find_files("G5_Trial_AA1_BEGIN","/Users/anandswaroop/Documents/test/C0Applets/AA_material-daatshf6")
#dest_dir
#MAIN = path #paste your dest directory here
#src_dir
# DIRS = r'C:\Users\sandy\Downloads\Documents\TeX SBs\M3C14\SA' #paste your source directory here
#if the dest file is deleted or not found make this code column as comment
#delete old file

del_file=os.path.join(path[0], "G5_Trial_AA1_BEGIN") #rename with the file in dest directory
os.remove(del_file)
#dest_dir = src_dir+"/subfolder"
#src_file = os.path.join(DIRS, 'G6_C26-SA-8.png') #rename with the file in source directory
#copy the file to destination dir
#shutil.copy(src_file, MAIN)
#if rename is not needed make this column as comment
#dst_file = os.path.join(MAIN,'G6_C26-SA-8.png') #rename with file in destinaion directory
#new_dst_file_name = os.path.join(MAIN, 'G6_C15_AA2-2.png') #rename with the file
#os.rename(dst_file, new_dst_file_name)#rename
#os.chdir(MAIN)
#print(os.listdir())