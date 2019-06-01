all_doc = []
for line in open("al_rdf_withType_set.txt", encoding='utf-8'):
    line = line.replace('\n','')
    all_doc.append(line)
clear_data = set(all_doc)
f = open("al_rdf_withType_set_clear.txt", "a+", encoding='utf-8')

for element in clear_data:
    f.write(element + '\n')
