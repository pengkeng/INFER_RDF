from gensim import corpora, models, similarities

all_doc_list = []
all_type_list = []
dictionary = dict
tfidf = []
index = []
INIT = False


def init():
    all_doc = []
    for line in open("set_test.txt", encoding='utf-8'):
        all_doc.append(line),

    for doc in all_doc:
        list = doc.split(":---->>>")
        doc_data = list[0].replace("\n", ' ').replace("[", " ").replace("]", " ").replace(",", " ")
        doc_list = doc_data.split()
        all_doc_list.append(doc_list)
        all_type_list.append(list[1])
    dictionary = corpora.Dictionary(all_doc_list)
    dictionary.keys()
    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
    tfidf = models.TfidfModel(corpus)
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    return dictionary, tfidf, index, True


def get_most_type_by_data(list, count):
    global dictionary, index, tfidf, INIT
    if INIT is False:
        dictionary, tfidf, index, INIT = init()
    doc_test_list = list.split()
    doc_test_vec = dictionary.doc2bow(doc_test_list)
    sim = index[tfidf[doc_test_vec]]
    a = sorted(enumerate(sim), key=lambda item: -item[1])
    i = 0
    result = []
    for item in a:
        i = i + 1
        if i > count:
            break
        element = []
        element.append(item)
        element.append(all_doc_list[item[0]])
        element.append(all_type_list[item[0]])
        result.append(element)
    return result


doc_test_list = '[year,month,day]'.replace("\n", ' ').replace("[", " ").replace("]", " ").replace(",", " ")
#
# print(get_most_type_by_data(doc_test_list, 10))
#
# print(get_most_type_by_data(doc_test_list, 20))
