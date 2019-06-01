# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET

from file import list_all_files
from release_rdf import list_all_child

rootdir = "F:\\xsd"
files = list_all_files(rootdir)

for file in files:
    file = file.replace('\n', '')
    try:
        f = open(file, encoding='utf-8')
        text = f.read()
        if text.__contains__('usbproduct') and text.__contains__('usbaddress') and text.__contains__('startupPolicy'):
            print(file)
        # if text.__contains__(
        #         'features') and text.__contains__('termination') and text.__contains__('devices') and text.__contains__(
        #     'devices') and text.__contains__('resources'):
        #     print(file)
    except:
        continue
