import csv
import tokenize
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
print(TreebankWordDetokenizer().detokenize(['the', 'quick', 'brown']))
				
data = []

#open and initialize files
file = open('process_s15.tsv.tokens.sents', 'r', encoding='utf-8').readlines()
output_file1 = open('clean.sents', 'w', newline='', encoding='utf-8')
#writer = csv.writer(output_file1, delimiter='\t')

# Read data line by line
for line in file:
	
	# split data by tab 
	# store it in list
	l=line.split('\t')
	
	# append list to ans
	data.append(l)
compsent= []
# print data line by line
for line in data:
	sent= line[1]
	words = sent.split()
	detokLine= TreebankWordDetokenizer().detokenize(words)
	if ' =' in detokLine:
		detokLine = detokLine.replace(" =", "=")
	if ' .' in detokLine:
		detokLine = detokLine.replace(" .", ".")
	compsent.append(detokLine)
			# tokens = tokenize.tokenize(words)
			# for token in tokens:
			# 	print(token)
			# if words[i]== 's':
			# 	words[i-1 : i] = [''.join(words[i-1 : i])]
			# 	writer.writerows(words)


for line in compsent:
	output_file1.write(line + '\n')

#close files
file.close()
output_file1.close()