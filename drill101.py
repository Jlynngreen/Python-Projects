

import os
import time

path = "C:\Python_Projects2"


list = os.listdir(path)
print(list)





for file in list:
    abpath = os.path.join(path, file) 
    if file.endswith(".txt"):
        print(file)
        modification_time = os.path.getmtime(abpath)
        local_time = time.ctime(modification_time) 
        print("Last modification time(Local time):", local_time) 
