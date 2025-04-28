from numpy.random.mtrand import Sequence
from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md
from textblob import TextBlob
# from translate import Translator
from googletrans import Translator
import asyncio
model = ru_core_news_md.load()


text = model(str(input()))
textlist = [word.lemma_ for word in text]


rutxt = ' '.join(textlist)

async def transtxt(text):
    translator = Translator()
    eng_txt = await translator.translate(text, src='ru', dest='en')


    return eng_txt

eng_text_after_func = asyncio.run(transtxt(rutxt))
print(eng_text_after_func.text)
res = TextBlob(eng_text_after_func.text).sentiment.polarity
print(res)

if res > 0:
    print('+')
elif res < 0:
    print('--')
else:
    print('+-')

#googletrans translator
