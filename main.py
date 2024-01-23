from google.cloud import translate_v2
import nltk
nltk.download('punkt')  
from nltk.tokenize import sent_tokenize
#from google.cloud import translate

import xml.etree.ElementTree as ET
english_sentences = 'en.txt'

xml_file_path = 'data\semeval-2015-task-13-en.xml'

try:
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    #Print the root element tag
    print("Root Element Tag:", root.tag)
    sentence_tags = root.findall('./sentence')

    # Extract and print sentences
    with open(english_sentences, 'w') as file:
        for text in root:
            for sentence in text:
                for wf in sentence:
                     file.write(f"{wf.text} ")
                file.write("\n")
                #print("  word:", wf.tag, "Value:", wf.text)
                #print(f"{wf.text} ", end='')
                
        # sentence = sentence_tag.text.strip()
            #word: {wf.get('id')}
        # if sentence:
        #     print(sentence)
except ET.ParseError as e:
    print(f"Error parsing XML file: {e}")
except FileNotFoundError:
    print(f"Error: File '{xml_file_path}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

credentials_path = 'central-phalanx-412008-d02d4f3c758d.json'
translate_client = translate_v2.Client.from_service_account_json(credentials_path)

def translate_text(text, target_language='en'):
    result = translate_client.translate(text, target_language=target_language)
    return result['input'], result['translatedText']

def translate_file(input_file, output_file, target_language='en'):
    output_file = open(output_file, 'w', encoding='utf-8')

    with open(input_file, 'r') as file:
        input_text = file.read()
        ip_sentences = sent_tokenize(input_text)
     
    for ip_sentence in ip_sentences:
        sentence, translated_text = translate_text(ip_sentence, target_language=target_language)
        output_file.write(translated_text)
        output_file.write("\n")
       
        

translate_file('en.txt', 'output.txt', target_language='bn')

