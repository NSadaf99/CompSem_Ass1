import csv
import babelnet as bn
from babelnet import BabelSynsetID
from babelnet import Language
from tqdm import tqdm

# we are using two dictionary files, open files
dict_file1 = open('BengaliDictionary_36.csv', 'r', encoding='utf-8')
dict_file2 = open('BengaliDictionary_93.csv', 'r', encoding='utf-8')
reader1 =csv.reader(dict_file1, delimiter=',')
dict_data1 = list(reader1)
reader2 =csv.reader(dict_file2, delimiter=',')
dict_data2 = list(reader2)

#Opening the file that contains output of translations, alignment and projection
data_file = open('ass2output_file1.tsv', 'r', encoding='utf-8')
reader =csv.reader(data_file, delimiter='\t')
tsv_data = list(reader)

#combine two dictionaries and clean
combined_dict = sorted(dict_data1 + dict_data2)


#create combined dictionary file
output_file = open("combined_dict", 'w', newline='', encoding='utf-8')
eng_dict = []
beng_dict = []
for eng, beng, comma1, comma in combined_dict:
    #for eng, comma, beng, comma in items:
    if len(eng.split())==1 and eng.isalnum():
        bengl= beng.split(',')
        eng_dict.append(eng.lower())
        beng_dict.append(bengl)
        output_file.write(eng.lower()+ '\t' + beng + '\n')

#out_row list will contain the synsets of the target language
out_row = []
#go through each row in ass2output_file1.tsv
for row in tsv_data:
    #go through each entry in combined_dict
    for bn_word, en_word in zip(beng_dict, eng_dict):
        flag = 0
        #go through each comma separated bengali meaning
        for meanings in bn_word:
            if(row[5] in meanings) and (row[1] in en_word):
                match = row[4]
                #flag set when meaning is found
                flag = 1
                break
        # if(flag == 0):
        #     for meanings in bn_word:
        #         if(row[5])  in meanings:
        #             match = (row[1] + '\t' + row[5]+'\t' + meanings + '\t'+ en_word)
        #             flag = 1
        #             break
            
        #if meaning already found
        if flag == 1:
                break
    if flag == 1:
        out_row.append(match)
    if flag == 0 :
        out_row.append('n/a')
    
    
#add new column to the original tsv data
for i, row in enumerate(tsv_data):
    row.append(str(out_row[i]))

#create a file where tokens will be written   
token = open("A2tokens.tsv", 'w', newline='', encoding='utf-8')

#checking if out_row has any matches
# for d in out_row:
#     token.write(d + '\n')

#write combined token data into a2tokens.tsv file
writer = csv.writer(token, delimiter='\t')
writer.writerows(tsv_data)

#close files
dict_file1.close()
dict_file2.close()
data_file.close()
output_file.close()
token.close()