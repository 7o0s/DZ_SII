#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import datetime

import re
from datetime import datetime

def find_date(string):
    pattern = r'\b(January|Jan.|Jan|February|Feb|Feb.|March|Mar|Mar.|April|Apr|Apr.|May|June|Jun|Jun.|July|Jul|Jul.|August|Aug|Aug.|September|Sep|Sept.|October|Oct|Oct.|November|Nov|Nov.|December|Dec|Dec.)\s\d{1,2},\s\d{4}\b'
    match = re.search(pattern, string)
    if match:
        return match.group()
    else:
        return None


def convert_date(date_str):
    date = find_date(date_str)
    print(date)
    print(date_str)
    if date is None:
        if date_str[0:5] == "Sept.":
            date_str = "Sep." + date_str[5:]
    # if date_str == "Sept. 15, 2021":
    #     date_str = "Sep. 15, 2021"
    # if date_str == "Sept. 22, 2008":
    #     date_str = "Sep. 22, 2008"
        date_formats = ["%b %d, %Y", "%d %B %Y", "%d %b %Y", "%B %d, %Y", "%d/%m/%Y", "%Y-%m-%d", "%d.%m.%Y", "%b. %d, %Y", "%B. %d, %Y", "%b. %d, %Y,", "on %B %d, %Y", "Bohn on %B %d, %Y", "%B %d, %Y,", "Hatchett on %b. %d, %Y"]
        for date_format in date_formats:
            try:
                date_obj = datetime.strptime(date_str, date_format)
                return date_obj.strftime("%d.%m.%Y")
            except ValueError:
                pass
        raise ValueError("Invalid date format")
    else:
        date = str(date)
        if date[0:5] == "Sept.":
            date = "Sep." + date[5:]
        date_formats = ["%b %d, %Y", "%d %B %Y", "%d %b %Y", "%B %d, %Y", "%d/%m/%Y", "%Y-%m-%d", "%d.%m.%Y",
                        "%b. %d, %Y", "%B. %d, %Y", "%b. %d, %Y,", "on %B %d, %Y", "Bohn on %B %d, %Y", "%B %d, %Y,",
                        "Hatchett on %b. %d, %Y"]
        for date_format in date_formats:
            try:
                date_obj = datetime.strptime(str(date), date_format)
                return date_obj.strftime("%d.%m.%Y")
            except ValueError:
                pass
        raise ValueError("Invalid date format")



# In[ ]:


print(convert_date("Sept. 15, 2021"))


# In[4]:


import os
import json

folder_path = "dataset_indexed" #путь к датасету самому
#folder_list = os.listdir(folder_path)
#folder_list_2 = os.listdir(folder_list[1].path)
#for f in folder_list[1]:
    
#folder_count = len(folder_list)
counter = 0
#print(folder_list.path)
subfolders = [f.path for f in os.scandir(folder_path)]
#print(subfolders)
for subfolder in subfolders[1:2]:
    subsubfolders = [m.path for m in os.scandir(subfolder)]
    for subsubfolder in subsubfolders[1:]:
        if subsubfolder != 'dataset_indexed\\review_directory_indexed\\.DS_Store':
            file_list = os.scandir(subsubfolder)
            file_list_count = len(os.listdir(subsubfolder))
            #print(file_count)
            for file in file_list:
                #print(file.path)
                with open (file, 'r') as f:
                    d = json.load(f)
                    f.close()

                if "date" in d and d["date"] != 'TBA - Early Access' and d["date"] != 'TBA':
                    counter = counter + 1
                    print(str(subsubfolder) + str(file))
                    print(d["date"])
                    d["date"] = convert_date(d["date"])
                    print("Заменил")
                    print(d["date"])
                    print(counter)
                    print("______________")
                else:
                    if "data" in d:
                        counter = counter + 1
                        print(str(subsubfolder) + str(file))
                        print(d["data"])
                        d["data"] = convert_date(d["data"])
                        print("Заменил")
                        print(d["data"])
                        print(counter)
                        print("______________")
                    else:
                        print("Не нашлось даты!!")
                        print(d)
                        with open("C:/Users/Маркин Алексей/Juptr/date unification/Унификация_даты_нет_даты.txt", "a") as outfile:
                            outfile.write(str(subsubfolder) + '/' + str(file))
                with open(file, 'w') as f:
                    f.write(json.dumps(d))
                    f.close()

    #             with open (file, 'r') as f:
    #                 d = json.load(f)
    #                 print(d)





