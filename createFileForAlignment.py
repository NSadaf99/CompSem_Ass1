import nltk
nltk.download('punkt')  
from nltk.tokenize import word_tokenize

#list concat_sent will have sentences in the format "english sentence ||| bengali sentence"
concat_sent = []  
concat_file = open('A2enbn.txt', 'w', encoding='utf-8')  

#open english cleaned sentences and translated sentences
beng = open('translatedTextHasanNMT.detok', 'r', encoding='utf-8').readlines()
eng = open('clean.sents', 'r', encoding='utf-8').readlines()

#open 2.5M corpus from hasan et.al
nmteng = open('original_corpus.en', 'r', encoding='utf-8').readlines()
nmtbeng = open('original_corpus.bn', 'r', encoding='utf-8').readlines()
count_translated_sentence = 0

#add english and bengali sentences
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

#add corpus english and bengali sentences
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

#close files
concat_file.close()
beng.close()
eng.close()
nmteng.close()
nmtbeng.close()