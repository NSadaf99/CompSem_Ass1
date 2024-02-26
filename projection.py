import csv


concat_file = open('A2enbn.txt', 'r', encoding='utf-8').readlines()

# Open the TSV file
sense_file = open('process_s15 - process_s15.tsv', 'r', encoding='utf-8')
reader =csv.reader(sense_file, delimiter='\t')
tsv_data = list(reader)
    
#output_file1 is tsv file with an additional column of aligned bangla word
output_file1 = open("A2tokens.tsv", 'w', newline='', encoding='utf-8')

#output_file2 is txt file with three tab separated columns
#format = "English sentence    Bengali sentence    word-level alignment"
output_file2 = open("A2sentences.tsv", 'w', encoding='utf-8')

#full_final.txt contains alignments obtained from fast_align
full_final = open("A2align.txt", 'r', encoding='utf-8').readlines()
output_bn = []


#projecting the sense annotations over the alignment links
#go through last 138 sentences (semeval sentences) and create both output files
for i in range (len(full_final)):

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
                bn_word = bn_sent[min(align_bn[index], len(bn_sent)-1)].strip()

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
#concat_file.close()
sense_file.close()
#full_final.close()
output_file1.close()
output_file2.close()