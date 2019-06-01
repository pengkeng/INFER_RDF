import xml.etree.ElementTree as ET

from getTypeTest import getFileword
from release_rdf import list_all_child
from tf_idf import get_most_type_by_data

file = "C:\\Users\\PQC\\Desktop\\mondial.xsd"
tree = ET.parse(file)
root = tree.getroot()
List = list_all_child(root)
wordList = List[0]
filewordlist = []
filetypelist = set()
getfile = getFileword(file)

print("--------------------" + file + "------------------------------")
print("---------------------原始数据----------------------------------")

for item in getfile:
    print(item)
    filewordlist.append(item.split()[0])

print("----------------------------------------------------------------")
print("---------------------推理结果-----------------------------------")

for line in wordList:
    doc_test_list = line.replace("\n", ' ').replace("[", " ").replace("]", " ").replace(",", " ")
    list = doc_test_list.split()
    result_list = get_most_type_by_data(doc_test_list, 10)
    for a in result_list:
        element = a[2].replace(":DATATYPE:", " ").replace(",", " ").split()
        for i in element:
            filetypelist.add(i)
    for item in list:
        result = get_most_type_by_data(item, 1)
        for a in result:
            element = a[2].replace(":DATATYPE:", " ").replace(",", " ").split()
            for i in element:
                filetypelist.add(i)

reslutlist = set()
for i in filetypelist:
    list = i.split("->")
    word = list[0]
    type = list[1]
    if (word in filewordlist and type != "null"):
        reslutlist.add(word + " " + type)

wordandtype = []
for word in filewordlist:
    item = word
    for type in reslutlist:
        if (word == type.split()[0]):
            item = item + " " + type.split()[1]
    wordandtype.append(item)
for item in wordandtype:
    print(item)
