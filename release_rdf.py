# -*- coding: UTF-8 -*-
import re
import xml.etree.ElementTree as ET


def list_child(root, word, type):
    word += '['
    for child in root:
        tag = re.sub(u"\\{.*?\}", "", child.tag)
        # if (tag == "element" or tag == "complexType" or tag == "simpleType"):
        if 'name' in child.attrib:
            tag = child.attrib['name']
        #     else:
        #         tag = ""
        # if (tag == "attribute"):
        #     continue
        if (tag is not ""):
            word += tag + ","
            if 'type' in child.attrib:
                type += tag + "->" + child.attrib['type'] + ","
            else:
                type += tag + "->null,"
        word, type = list_child(child, word, type)
    word += ']'
    return word, type


def list_all_child(root):
    word_list = []
    type_list = []
    for child in root:
        word = "["
        type = ''
        tag = re.sub(u"\\{.*?\}", "", child.tag)
        # if (tag == "element" or tag == "complexType" or tag == "simpleType"):
        if 'name' in child.attrib:
            tag = child.attrib['name']
        #     else:
        #         tag = ""
        # if (tag == "attribute"):
        #     continue
        if (tag is not ""):
            word += tag
            if 'type' in child.attrib:
                type += tag + "->" + child.attrib['type'] + ","
            else:
                type += tag + "->null,"
        word, type = list_child(child, word, type)
        word += "]"
        word = word.replace("[]", "")
        word = word.replace(",]", "]")
        word = word.replace(",[", "[")
        word = re.sub(u"\\{.*?\}", "", word)
        word_list.append(word)
        type_list.append(type)
    return word_list, type_list

# def get_rdf_element(file):
#     try:
#         tree = ET.parse(file)
#         root = tree.getroot()
#         return list_all_child(root)
#     except IOError:
#         print("FILEERROR")
