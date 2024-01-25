from google.cloud import translate_v2
import nltk
nltk.download('punkt')  
from nltk.tokenize import word_tokenize
#from google.cloud import translate

import xml.etree.ElementTree as ET
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

#credentials for google cloud translate
credentials_path = 'central-phalanx-412008-d02d4f3c758d.json'
translate_client = translate_v2.Client.from_service_account_json(credentials_path)

#concat file contains lines of the format "english sentence ||| bangla sentence"
#file name enbn.txt
concat_sent = []  
concat_file = open('enbn.txt', 'w', encoding='utf-8')  

#translate_text function makes call to translate client
def translate_text(text, target_language='en'):
    result = translate_client.translate(text, target_language=target_language)
    return result['input'], result['translatedText']

#translate file function opens input file, reads it and adds to concat file
def translate_file(input_file, output_file, target_language='en'):
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
    
    for sent in concat_sent:
        concat_file.write(sent)

    concat_file.close()
       
#open the data files from OPUS
bnop_file = open('bn_opus.txt', 'r', encoding='utf-8')
enop_file = open('en_opus.txt', 'r', encoding='utf-8')

#add the OPUS data into the concat file
for bn_line, en_line in zip(bnop_file, enop_file):
    concat_sent.append(' '.join(word_tokenize(en_line.strip())) + ' ||| ' + ' '.join(word_tokenize(bn_line.strip())) +'\n')
        
#files closed
bnop_file.close()
enop_file.close()
translate_file('en.txt', 'bn.txt', target_language='bn')
