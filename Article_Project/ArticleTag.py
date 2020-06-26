class ReadArticle:
    def GetArticleData(self, file_Name):
        file_data = open(file_Name, 'r')
        return file_data.readlines()

class WriteArticleTag:
    def WriteArticleTag(self,file_Name,data):
        file = open(file_Name,"a")
        file.write(data)
        file.close()


from sklearn.feature_extraction.text import CountVectorizer
import scipy
from sklearn.feature_extraction import text
ReadArticleObj = ReadArticle()
article1Data = ReadArticleObj.GetArticleData('Articles\Article1.txt')

# Create an object of count vectorizer
cv = CountVectorizer(stop_words=text.ENGLISH_STOP_WORDS)
# fit, training our algorithm
sentense = []
stringvalue = ""
for temp in article1Data:
    stringvalue = stringvalue + temp
sentense.append(stringvalue)
print(sentense)
counts = cv.fit_transform(sentense)
bows = cv.vocabulary_
print(counts)
print(bows)

Article1Write = WriteArticleTag()


coo = scipy.sparse.coo_matrix(counts)
for _count, bowname in zip(coo.data,bows.keys()):
    Article1Write.WriteArticleTag("Article1_Bow_Tag.txt",str(_count) + " -- "+bowname+"\n")

print("Done")
#Write Data
