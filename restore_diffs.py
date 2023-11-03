from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import diff_match_patch as dmp_module

orig_path = askdirectory(title="Select folder with original code")
diff_path = askdirectory(title="Select folder with the delta files")

files = {}

for filename in os.listdir(diff_path):
    filename = filename[:-6] + ".gml"
    orig_file = os.path.join(orig_path, filename)
    if os.path.isfile(orig_file):
        filename = filename[:-4] + ".patch"
        diff_file = os.path.join(diff_path, filename)
        files[orig_file] = diff_file

for orig_file_path, diff_file_path in files.items():
    with open(orig_file_path, 'r') as orig_file, open(diff_file_path, 'r') as diff_file:
        orig_data = orig_file.read()
        diff_data = diff_file.read()
        
    dmp = dmp_module.diff_match_patch()
    
    orig_lines = ''.join(orig_data)
    diff_lines = ''.join(diff_data)
    patch = dmp.patch_fromText(diff_lines)
    result = dmp.patch_apply(patch, orig_lines)
    
    file_name = os.path.basename(orig_file_path)
    if not os.path.isdir("./code"):
        os.mkdir("./code")
    final_file = open("./code" + '/' + file_name, 'w')
    final_file.write(result[0])
    final_file.close()
