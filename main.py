# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET

from file import list_all_files
from release_rdf import list_all_child

rootdir = "F:\\xsd_test"
files = list_all_files(rootdir)
f = open("all_rdf_withType_set_clear_test.txt", "a+", encoding='utf-8')

# filelsit = open("filenameList.txt", "a+", encoding='utf-8')
# files = []
# line = filelsit.readline()  # 调用文件的 readline()方法
# for line in open("filenameList.txt", encoding='utf-8'):
#     files.append(line),

for file in files:
    file = file.replace('\n', '')
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        List = list_all_child(root)
        print(file)
        wordList = List[0]
        typeList = List[1]
        data_set = set()
        for index in range(len(wordList)):
            data_set.add(wordList[index] + ":---->>>:DATATYPE: " + typeList[index])
    except:
        print("FILEERROR" + file)
        continue
    for element in data_set:
        f.write(element + '\n')

f.close()
