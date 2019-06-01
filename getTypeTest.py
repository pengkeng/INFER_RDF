import xml.etree.ElementTree as ET

from release_rdf import list_all_child


def getFileword(file):

    tree = ET.parse(file)
    root = tree.getroot()
    List = list_all_child(root)
    wordList = List[0]
    typeList = List[1]

    list = set()
    for index in range(wordList.__len__()):
        wordline = wordList[index].replace("\n", ' ').replace("[", " ").replace("]", " ").replace(",", " ").split()
        typeline = typeList[index].replace("\n", ' ').replace("[", " ").replace("]", " ").replace(",", " ").split()
        for i in range(wordline.__len__()):
            word = wordline[i]
            type = typeline[i].split("->")
            if (word == type[0] and type[1] != 'null'):
                # print(word, type[1])
                list.add(word +" "+type[1])
    return list
