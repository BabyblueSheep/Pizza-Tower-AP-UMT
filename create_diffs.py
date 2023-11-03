from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import diff_match_patch as dmp_module

orig_path = askdirectory(title="Select folder with original code")
modif_path = askdirectory(title="Select folder with modified code")

files = {}

for filename in os.listdir(modif_path):
    orig_file = os.path.join(orig_path, filename)
    if os.path.isfile(orig_file):
        modif_file = os.path.join(modif_path, filename)
        files[orig_file] = modif_file

for orig_file_path, modif_file_path in files.items():
    with open(orig_file_path, 'r') as orig_file, open(modif_file_path, 'r') as modif_file:
        orig_data = orig_file.read()
        modif_data = modif_file.read()

    dmp = dmp_module.diff_match_patch()

    orig_lines = ''.join(orig_data)
    modif_lines = ''.join(modif_data)
    patch = dmp.patch_make(orig_lines, modif_lines)
    result = dmp.patch_toText(patch)
    
    file_name = os.path.basename(orig_file_path)
    if not os.path.isdir("./diffs"):
        os.mkdir("./diffs")
    delta_file = open("./diffs" + '/' + file_name[:-4] + ".patch", 'w')
    delta_file.write(result)
    delta_file.close()
