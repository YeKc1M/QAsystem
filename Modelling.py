import nltk
from gensim import corpora, models, similarities
from QuestionParser import QuestionParser

qp=QuestionParser()

lemmatizer=nltk.stem.wordnet.WordNetLemmatizer()
noun_tags=['NN','NNS','NNP','NNPS']
verb_tags=['VB','VBD','VBG','VBN','VBP','VBZ']

def cleanCorpora(texts):
    stopwords=[',','/','the']
    tokens_list=[]
    for text in texts:
        tokens_list.append(nltk.word_tokenize(text))
    cleaned_tokens_list=[]
    for tokens in tokens_list:
        tagged_tokens=nltk.pos_tag(tokens)
        cleaned_tokens=[]
        for token, tag in tagged_tokens:
            if token not in stopwords:
                t=token
                if tag in noun_tags:
                    t=lemmatizer.lemmatize(token, 'n').lower()
                if tag in verb_tags:
                    t=lemmatizer.lemmatize(token, 'v').lower()
                cleaned_tokens.append(t)
        cleaned_tokens_list.append(cleaned_tokens)
    # print(cleaned_tokens_list)
    return cleaned_tokens_list

corp=qp.getAllNames()
# print(corp)
# print(len(corp))
cleaned_tokens_list=cleanCorpora(corp)
# print(cleaned_corp)

def calculateSimilarity(clean_tokens_list, query):
    dictionary=corpora.Dictionary(clean_tokens_list)
    bow_corpus=[dictionary.doc2bow(clean_tokens) for clean_tokens in clean_tokens_list]
    tfidf=models.TfidfModel(bow_corpus)
    # print(tfidf[dictionary.doc2bow('explore knowldege sources step 1'.split(' '))])
    index=similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=len(dictionary))

    query_bow=dictionary.doc2bow(query.split(' '))
    sims=index[tfidf[query_bow]]
    return sims

# sims=calculateSimilarity(cleaned_tokens_list, 'explore knowledge sources step 1')
# print(sorted(enumerate(sims), key=lambda x: x[1], reverse=True)[0])

def calculateAllNames(query):
    return calculateSimilarity(cleaned_tokens_list, query)