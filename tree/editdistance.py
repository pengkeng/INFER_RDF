# -*- coding: UTF-8 -*-
import re
import xml.etree.ElementTree as ET

from matplotlib import get_label
from zss import Node, distance, AnnotatedTree

try:
    from editdist import distance as strdist
except ImportError:
    def strdist(a, b):
        if a == b:
            return 1
        else:
            return 0


def weird_update_dist(A, B):
    return strdist(A,B)


def weird_insert_dist(A):
    return 1


def weird_remove_dist(A):
    return 1


class WeirdNode(object):

    def __init__(self, label):
        self.my_label = label
        self.my_children = list()

    @staticmethod
    def get_children(node):
        return node.my_children

    @staticmethod
    def get_label(node):
        return node.my_label

    def addkid(self, node, before=False):
        if before:
            self.my_children.insert(0, node)
        else:
            self.my_children.append(node)
        return self


def setNode(root, node):
    treelist = []
    for child in root:
        tag = re.sub(u"\\{.*?\}", "", child.tag)
        if 'name' in child.attrib:
            tag = child.attrib['name']
        subnode = WeirdNode(tag)
        setNode(child, subnode)
        treelist.append(subnode)
    for item in treelist:
        node.addkid(item)
    return


def get_distance(file_a, file_b):
    tree_a = ET.parse(file_a)
    root_a = tree_a.getroot()
    A = WeirdNode("a")
    setNode(root_a, A)

    tree_b = ET.parse(file_b)
    root_b = tree_b.getroot()
    B = WeirdNode("a")
    setNode(root_b, B)
    b = AnnotatedTree(B, WeirdNode.get_children)
    if len(b.nodes) > 200:
        return 100000
    return distance(A, B, WeirdNode.get_children, weird_insert_dist, weird_remove_dist, weird_update_dist)

