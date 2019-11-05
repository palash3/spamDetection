# Just import them and use it
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
dirty_text = "He studies in the house yesterday, unluckily, the fans breaks down"
def word_stemmer(words):
    stem_words = [stemmer.stem(o) for o in words]
    return " ".join(stem_words)
def word_lemmatizer(words):
   lemma_words = [lemmatizer.lemmatize(o) for o in words]
   return " ".join(lemma_words)


clean_text = word_stemmer(dirty_text.split(" "))
clean_text = word_lemmatizer(dirty_text.split(" "))
print(clean_text)
#Output
'He studi in the hous yesterday, unluckily, the fan break down'