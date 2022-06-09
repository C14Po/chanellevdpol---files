__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile

path = os.path.dirname(__file__)
folder = '\cache'
new_folder = path + folder
zip_path = path + '\data.zip'

def clean_cache():
    if os.path.exists(new_folder):
       shutil.rmtree(new_folder)
       os.mkdir(new_folder)
    else: 
        os.mkdir(new_folder) 

def cache_zip(zip, cachedir):
    with ZipFile(zip, 'r') as file:
        file.extractall(cachedir)

def cached_files():
    list = os.listdir(new_folder)
    empty_list = []
    for i in list:
        path = os.path.join(new_folder, i)
        if os.path.isfile(path):
            empty_list.append(path)
    return empty_list

list = cached_files()

def find_password(list):
    for i in list:
        with open(i) as f:
           contents = f.readlines()
           for i in contents:
               if "password" in i:
                    password_return = i.removeprefix('password: ')
                    return password_return.rstrip('\n')

clean_cache()
cache_zip(zip_path, new_folder)
cached_files()
find_password(list)