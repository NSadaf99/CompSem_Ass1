from google.cloud import translate_v2
import nltk
import csv
nltk.download('punkt')  
from nltk.tokenize import word_tokenize
import xml.etree.ElementTree as ET

#funtion that reads xml data file and writes english data into the 'en.txt' file
def read_xml():
    
    english_sentences = 'en.txt'
    xml_file_path = 'data\semeval-2015-task-13-en.xml'

    try:
        # Parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        #find all xml element tags
        sentence_tags = root.findall('./sentence')

        # Extract and write sentences into file en.txt
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


#comment this to avoid re-reading xml file for later runs
read_xml()


#credentials for google cloud translate
#credentials file not commited to github since posting it online not allowed by google
credentials_path = 'central-phalanx-412008-d02d4f3c758d.json'
translate_client = translate_v2.Client.from_service_account_json(credentials_path)

#concat file contains lines of the format "english sentence ||| bengali sentence"
#concat file name is enbn.txt
concat_sent = []  
concat_file = open('enbn.txt', 'w', encoding='utf-8')  
count_translated_sentence = 0

#translate_text function makes call to translate client
def translate_text(text, target_language='en'):
    result = translate_client.translate(text, target_language=target_language)
    return result['input'], result['translatedText']

#translate file function opens input file, translates it, adds to concat file, returns number of translated sentences
def translate_file(input_file, output_file, count_translated_sentence, target_language='en'):
    output_file = open(output_file, 'w', encoding='utf-8')

    #read english file and put sentences into list ip_sentences
    with open(input_file, 'r') as file:
        input_text = file.read()
        ip_sentences = input_text.splitlines()
 
    #send each sentence through translate_text function
    for ip_sentence in ip_sentences:
        sentence, translated_text = translate_text(ip_sentence, target_language=target_language)
        #write each translated sentence into bn.txt
        output_file.write(translated_text)

        #create concat_sent list in the format "english sentence ||| bengali sentence"
        if (sentence and translated_text):
            concat_sent.append(sentence + '||| ' + translated_text +'\n')
            output_file.write("\n")
        count_translated_sentence = count_translated_sentence + 1

    #write into concat file 
    #file format = "english sentence ||| bengali sentence"
    #file name = enbn.txt
    for sent in concat_sent:
        concat_file.write(sent)

    #close files
    concat_file.close()
    output_file.close()

    #ret count_translated_sentence
    return count_translated_sentence

#function to add OPUS data to the concat sentences
def add_OPUS_data():

    #open the data files from OPUS
    #these data files serve as extra training data
    bnop_file = open('bn_opus.txt', 'r', encoding='utf-8')
    enop_file = open('en_opus.txt', 'r', encoding='utf-8')

    #add the OPUS data with the previously extracted data
    for bn_line, en_line in zip(bnop_file, enop_file):
        concat_sent.append(' '.join(word_tokenize(en_line.strip())) + ' ||| ' + ' '.join(word_tokenize(bn_line.strip())) +'\n')
        
    #files closed
    bnop_file.close()
    enop_file.close()

#OPUS data added to concat sentences first
#comment this to save time for later runs
add_OPUS_data()

#sentences translated and translated data added to concat sentences
#comment this to save time for later runs
count_translated_sentence = translate_file('en.txt', 'bn.txt', count_translated_sentence, target_language='bn')

#uncomment to save time for later runs
#count_translated_sentence = 138

#open concat file containing OPUS and extracted semeval data
concat_file = open('enbn.txt', 'r', encoding='utf-8').readlines()

# Open the TSV file
sense_file = open('process_s15 - process_s15.tsv', 'r', encoding='utf-8')
reader =csv.reader(sense_file, delimiter='\t')
tsv_data = list(reader)
    
#output_file1 is tsv file with an additional column of aligned bangla word
output_file1 = open("output_file1.tsv", 'w', newline='', encoding='utf-8')

#output_file2 is txt file with three tab separated columns
#format = "English sentence    Bengali sentence    word-level alignment"
output_file2 = open("output_file2.txt", 'w', encoding='utf-8')

#full_final.txt contains alignments obtained from fast_align
full_final = open("full_final.txt", 'r', encoding='utf-8').readlines()
output_bn = []


#projecting the sense annotations over the alignment links
#go through last 138 sentences (semeval sentences) and create both output files
for i in range (len(concat_file) - count_translated_sentence, len(concat_file)):

    #extract alignments obtained from fast_align
    align_sent = full_final[i]

    #extract english(en) and bengali(bn) sentences
    sent = concat_file[i]
    en, bn = sent.split("||| ")
    en = en.strip()
    bn = bn.strip()

    #write into output_file2
    output_file2.write(en + '\t' + bn + '\t' + align_sent.strip() + '\n')
   
    #word level tokenization
    en_sent = en.split(" ")
    bn_sent = bn.split(" ")
    alignments = align_sent.split()
    
    #align_en contains all english alignment positions
    #align_bn contains all bengali alignment positions
    align_en = [int(pair.split('-')[0]) for pair in alignments]
    align_bn = [int(pair.split('-')[1]) for pair in alignments]
  
   #go through each word in sentence
    word_position_pairs = [(word, position) for position, word in enumerate(en_sent)]
    for word, position in word_position_pairs:
        flag = 0

        #go through each alignment
        for index in range(len(align_en)):

            #if word exits in alignment
            if position == align_en[index]:
                flag = 1
                bn_word = bn_sent[align_bn[index]].strip()

        #add n/a if word not in alignment
        if(flag == 0):
            output_bn.append('n/a')
        else:
            output_bn.append(bn_word)

            
#add new column to the original tsv data
for i, row in enumerate(tsv_data):
    row.append(str(output_bn[i]))

#write into output_file1.tsv
writer = csv.writer(output_file1, delimiter='\t')
writer.writerows(tsv_data)

#close files
concat_file.close()
sense_file.close()
full_final.close()
output_file1.close()
output_file2.close()