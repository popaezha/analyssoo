from numpy.random.mtrand import Sequence
from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md
from textblob import TextBlob
# from translate import Translator
from googletrans import Translator
model = ru_core_news_md.load()



text = model('Отличный фильм')
textlist = [word .lemma_ for word in text]





# erevod = Translator(from_lang='Russian', to_lang="English")
# eng_txt = perevod.translate(ru_txt)
# print(eng_txt)

perevod = Translator(proxy="https://translate.googleapis.com/translate_a/single")
ru_txt = ' '.join(textlist)
eng_txt = perevod.translate(ru_txt)
print(eng_txt)

res = TextBlob(eng_txt).sentiment.polarity
print(res)

if res > 0:
    print('+')
elif res < 0:
    print('--')
else:
    print('+-')

#googletrans translator
