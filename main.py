from google.cloud import translate_v2
import nltk
import csv
nltk.download('punkt')  
from nltk.tokenize import word_tokenize
#from google.cloud import translate
import xml.etree.ElementTree as ET
def read_xml():
    
    english_sentences = 'en.txt'

    xml_file_path = 'data\semeval-2015-task-13-en.xml'

    try:
        # Parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        #find all xml element tags
        sentence_tags = root.findall('./sentence')

        # Extract and write sentences in file en.txt
        with open(english_sentences, 'w') as file:
            for text in root:
                for sentence in text:
                    for wf in sentence:
                         file.write(f"{wf.text} ")
                    file.write("\n")
                    
    #expception handling
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except FileNotFoundError:
        print(f"Error: File '{xml_file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
#comment
read_xml()
#credentials for google cloud translate
credentials_path = 'central-phalanx-412008-d02d4f3c758d.json'
translate_client = translate_v2.Client.from_service_account_json(credentials_path)

#concat file contains lines of the format "english sentence ||| bangla sentence"
#file name enbn.txt
concat_sent = []  
concat_file = open('enbn.txt', 'w', encoding='utf-8')  
count_translated_sentence = 0
#translate_text function makes call to translate client
def translate_text(text, target_language='en'):
    result = translate_client.translate(text, target_language=target_language)
    return result['input'], result['translatedText']

#translate file function opens input file, reads it and adds to concat file
def translate_file(input_file, output_file, count_translated_sentence, target_language='en'):
    output_file = open(output_file, 'w', encoding='utf-8')

    with open(input_file, 'r') as file:
        input_text = file.read()
        ip_sentences = input_text.splitlines()
 
    for ip_sentence in ip_sentences:
        sentence, translated_text = translate_text(ip_sentence, target_language=target_language)
        output_file.write(translated_text)
        if (sentence and translated_text):
            concat_sent.append(sentence + '||| ' + translated_text +'\n')
            output_file.write("\n")
        count_translated_sentence = count_translated_sentence + 1

    for sent in concat_sent:
        concat_file.write(sent)
        
    concat_file.close()
    return count_translated_sentence
       
#open the data files from OPUS
bnop_file = open('bn_opus.txt', 'r', encoding='utf-8')
enop_file = open('en_opus.txt', 'r', encoding='utf-8')

#add the OPUS data with the extracted data
for bn_line, en_line in zip(bnop_file, enop_file):
    concat_sent.append(' '.join(word_tokenize(en_line.strip())) + ' ||| ' + ' '.join(word_tokenize(bn_line.strip())) +'\n')
        
#files closed
bnop_file.close()
enop_file.close()
count_translated_sentence = translate_file('en.txt', 'bn.txt', count_translated_sentence, target_language='bn')


concat_file = open('enbn.txt', 'r', encoding='utf-8').readlines()
output_file1 = open("output_file1.tsv", 'w', newline='', encoding='utf-8')
output_file_txt= open("output_file1.txt", 'w', encoding='utf-8')
output_file2 = open("output_file2.txt", 'w', encoding='utf-8')
full_final = open("full_final.txt", 'r', encoding='utf-8').readlines()
output_bn = []
# Open the TSV file and read specific columns
sense_file = open('process_s15 - process_s15.tsv', 'r', encoding='utf-8')
#final_align_file = open('final_align.txt', 'r', encoding='utf-8')
reader =csv.reader(sense_file, delimiter='\t')
    
cnt= 1
#comment
count_translated_sentence = 138
for i in range (len(concat_file) - count_translated_sentence, len(concat_file)):
    sent = concat_file[i]
    align_sent = full_final[i]
    en, bn = sent.split("||| ")
    en = en.strip()
    bn = bn.strip()
    output_file2.write(en + '\t' + bn + '\t' + align_sent.strip() + '\n')
    en_sent = en.split(" ")
    bn_sent = bn.split(" ")
    alignments = align_sent.split()
    
    align_en = [int(pair.split('-')[0]) for pair in alignments]
    align_bn = [int(pair.split('-')[1]) for pair in alignments]
  
   
    word_position_pairs = [(word, position) for position, word in enumerate(en_sent)]
   
    for word, position in word_position_pairs:
        flag = 0
        for index in range(len(align_en)):
            #if word exits in alignment
            if position == align_en[index]:
                flag = 1
                bn_word = bn_sent[align_bn[index]].strip()

        if(flag == 0):
            output_bn.append('n/a')
        else:
            output_bn.append(bn_word)
    output_file_txt.write('\n')
    cnt = cnt+1






tsv_data = list(reader)

# Add the new column to the data
for i, row in enumerate(tsv_data):
    row.append(str(output_bn[i]))

# Writing the modified data back to the TSV file

writer = csv.writer(output_file1, delimiter='\t')
writer.writerows(tsv_data)


output_file1.close()
output_file2.close()