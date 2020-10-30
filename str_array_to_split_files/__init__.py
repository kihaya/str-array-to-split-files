#coding: utf-8

import os
import typing
import uuid

def str_array_to_split_files(data=[], target_directory="") -> bool:
    """
    Split string array to splitted files.
    """

    ext = ".txt"

    try:
       if len(os.listdir(target_directory)) > 0: return False
    except:
       return False

    if len(data) <= 0: return False

    for str_data in data:
        filename = str(uuid.uuid4())[:8]
        full_file_name = target_directory + "/" + filename + ext
        f = open(full_file_name, "w")
        f.write(str_data)
        f.close()

    return True
