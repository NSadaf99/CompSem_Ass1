import nltk
nltk.download('punkt')  
from nltk.tokenize import word_tokenize

concat_sent = []  
concat_file = open('myenbn.txt', 'w', encoding='utf-8')  
beng = open('RasingNews.pred-test.txt.detok', 'r', encoding='utf-8').readlines()
eng = open('output_file_clean.sents', 'r', encoding='utf-8').readlines()
nmteng = open('original_corpus.en', 'r', encoding='utf-8').readlines()
nmtbeng = open('original_corpus.bn', 'r', encoding='utf-8').readlines()
count_translated_sentence = 0

for i in range (len(eng)):
        sentence= eng [i].strip()
        sentence= " ".join(word_tokenize(sentence))
        translated_text = beng [i].strip()
        translated_text= " ".join(word_tokenize(translated_text))
        #create concat_sent list in the format "english sentence ||| bengali sentence"
        if (sentence and translated_text):
            concat_file.write(sentence + ' ||| ' + translated_text +'\n')
        count_translated_sentence = count_translated_sentence + 1
print(count_translated_sentence)
for j in range (len(nmteng)):
        sentence= nmteng [j].strip()
        translated_text = nmtbeng [j].strip()
        sentence= " ".join(word_tokenize(sentence))
        translated_text= " ".join(word_tokenize(translated_text))
        #create concat_sent list in the format "english sentence ||| bengali sentence"
        if (sentence and translated_text):
            concat_file.write(sentence + ' ||| ' + translated_text +'\n')
        count_translated_sentence = count_translated_sentence + 1

print(count_translated_sentence)