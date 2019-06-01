from gensim.models import word2vec

sentences = word2vec.LineSentence("./al_rdf_withType_set_clear.txt")
model = word2vec.Word2Vec(sentences, hs=1, min_count=1, window=1, size=100)
# print(sentences)

req_count = 5
for key in model.wv.similar_by_word('[DateYearBaseType[restriction[pattern]]]', topn=100):
    req_count -= 1
    print(key[0], key[1])
    if req_count == 0:
        break

# print(model.wv.n_similarity('[_5zkd-reze[rowID,member,incidentnumber,createdatetime,incidenttype,disposition,streetname,location[SpatialThing]]]', '[_5zkd-reze[rowID,member,incidentnumber,createdatetime,incidenttype,disposition,streetname,location[SpatialThing]]]'))


