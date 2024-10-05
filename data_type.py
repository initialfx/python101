#houdini = ["19.5.435", "19.5.682", '20.0.547', '20.5.278']
#houdini_dict = {"houdini":["19.5.435", "19.5.682", '20.0.547', '20.5.278']}

import os

path = "C:\Program Files\Side Effects Software"

houdini = os.listdir(path)

exclude_items = ['Houdini Server', 'License Server', 'sidefx_packages']


#for x in exclude_items:
    #houdini.remove(x)

def houdini_filter(houdini_list, exclude_items):
    for x in exclude_items:
        houdini_list.remove(x)

    temp_list = []

    for x in houdini_list:
        temp_list.append(x.split(" ")[1])
    
    return temp_list

def version_filter(version):
    pass


