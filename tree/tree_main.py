import datetime

from tree.editdistance import get_distance

files = []
min = 1000
filename = ""
starttime = datetime.datetime.now()

for line in open("../filenameList.txt", encoding='utf-8'):
    line = line.replace('\n','')
    files.append(line)
    # print(line)
    try:
        temp = get_distance("C:\\Users\\PQC\\Desktop\\可用数据\\Tron_(hacker).rdf", line)
        if temp is 0:
            print(line)
        if temp < min:
            min = temp
            filename = line
    except:
        continue
    if min is 0:
        break

print(filename)

endtime = datetime.datetime.now()
# for file in files:
#     print(get_distance("../rows.rdf", file))