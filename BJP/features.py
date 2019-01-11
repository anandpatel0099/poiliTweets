#from sklearn.linear_model import LogisticRegression
from sklearn import svm
#import pylab as pl
import numpy as np
#from sklearn import cross_validation
import operator
from sklearn.grid_search import GridSearchCV

s_words1 = ["a",":","$number$","&amp","&amp;","like" ,"about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
tweets = []
for line in open('BJP_train.txt').readlines():

    items_1 = line.split(',')

# print items
    tweets.append([int(items_1[0]), items_1[1].lower().strip()])


# Extract the vocabulary of keywords
vocabulary = dict()

for class_label_1, text_2 in tweets:
    for item in text_2.split():
        item = item.lower()
        if len(item) > 2 and item not in s_words1:
            if vocabulary.has_key(item):
                vocabulary[item] = vocabulary[item] + 1
            else:
                vocabulary[item] = 1

#arrange vocabulary of keywords in reverse order of frequency
vocabulary_2 = sorted(vocabulary.items(), key=operator.itemgetter(1), reverse=True)
vocabulary=dict()


#get 10 frequent words from tweets
for i in range(len(vocabulary_2)):
    if(i<10):
        vocabulary[vocabulary_2[i][0]] = vocabulary_2[i][1]


# produce an id  for each term in vocabulary id starts from 0
vocabulary = {item: idx for idx, (item, freq) in enumerate(vocabulary.items())}
print "10 features from given tweets:" + str(','.join(vocabulary.keys())) + "\n"


# Generate X and y
X = []
Y = []
for class_label_1, text_2 in tweets:
    p = [0] * len(vocabulary)
    terms = [item for item in text_2.split() if len(item) > 2]
    for item in terms:
        if vocabulary.has_key(item):
            p[vocabulary[item]] += 1
    Y.append(class_label_1)
    X.append(p)

a=np.asarray(X)
b = np.asarray(Y)
print "2 Dimensional array in which each row consist \"value for 10 features\" for each tweet (500 rows & 10 columns): "
print a
print "\n"
print "2 Dimensional array in which each row consist \"class label\" for each tweet(500 rows & 10 columns): "
print b
print "\n"


