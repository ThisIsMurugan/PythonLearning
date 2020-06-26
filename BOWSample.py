from sklearn.feature_extraction.text import  CountVectorizer
stopWords = []
stopWords.append("to")
sentence = ['I love to watch movies, especially action movies']
#Create an object of count vectorizer
cv = CountVectorizer(stop_words=stopWords)
# fit, training our algorithm
cv.fit(sentence)
cvt = cv.transform(sentence)

print(cv.vocabulary_)
print(cvt)
