# -*- coding: UTF-8 -*-
import re
import xml.etree.ElementTree as ET

from zss import Node, simple_distance
#
# from file import list_all_files
# from release_rdf import list_all_child
#
# # f = open("rowsTest.txt", "a+", encoding='utf-8')
# file = "./rows.rdf"
# tree = ET.parse(file)
# root = tree.getroot()
# # wordList = list_all_child(root)
# # for word in wordList:
# #     word = re.sub(u"\\{.*?\}", "", word)
# #
# #     f.writelines(word + '\n')
# # f.close()
# A = Node("a")
#
#
# def setNode(root, node):
#     treelist = []
#     for child in root:
#         tag = re.sub(u"\\{.*?\}", "", child.tag)
#         if 'name' in child.attrib:
#             tag = child.attrib['name']
#         subnode = Node(tag)
#         setNode(child, subnode)
#         treelist.append(subnode)
#     for item in treelist:
#         node.addkid(item)
#     return
#
#
# B = (
#     Node("f")
#         .addkid(Node("a")
#                 .addkid(Node("d"))
#                 .addkid(Node("c")
#                         .addkid(Node("b"))))
#         .addkid(Node("e"))
# )
#
# setNode(root,A)
# print(simple_distance(A, B))

all_doc = set()
for line in open("all_rdf_withType_set_clear_test.txt", encoding='utf-8'):
    all_doc.add(line)

f = open("set_test.txt", "a+", encoding='utf-8')

for element in all_doc:
    f.write(element)
