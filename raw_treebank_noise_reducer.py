from nltk.corpus import BracketParseCorpusReader
from nltk.corpus import ptb
import nltk
import string
from simpleparse.parser import Parser
import re

grammar = """integer := [0-9]+<alpha> := -integer+all     := (integer/alpha)+"""

def CorpusPTBReader(ptb_data_path):
    ptb_sent_file = open("total_ptb.txt", "w")

    file_pattern = r".*/.*\.mrg"

    ptb = BracketParseCorpusReader(ptb_data_path, file_pattern)
    #print (ptb.fileids())
    #print ((ptb.sents()))
    #ptb.sents(fileids= 'brown/cf/cf01.mrg')[0]
    count = 0
    for sent in ptb.sents():
        '''sent = ""
        for word in sent:
            if "\\" in word or "e_s" in word or "n_s" in word:
                continue
            else:
                sent += word + " "
        out = sent[:-1]'''
        if len(sent) < 7: continue
        out = ' '.join(sent)
        out = out.lower()
#        print(len(sent), out)

        parser = Parser(grammar, 'all')
        temp_result = parser.parse(out)
        sub_sent = []
        start_index = 0
        for num_info in temp_result[1]:
            sub_sent.append( out[start_index:num_info[1]] )
            sub_sent.append( "NUM"+(str(num_info[2]-num_info[1])))
            start_index = num_info[2]
        sub_sent.append( out[start_index:])
        final_out = ''.join(sub_sent)
        
        final_out = re.sub(r'\*\-NUM\d ', '', final_out)
        final_out = re.sub(r'e_s ', '', final_out)
        final_out = re.sub(r'n_s ', '', final_out)
        final_out = re.sub(r'e_s', '', final_out)
        final_out = re.sub(r'n_s', '', final_out) 
        final_out = re.sub(r'\\. ', '', final_out)
        final_out = re.sub(r'\\.', '', final_out)
        final_out = re.sub(r'\*. ', '', final_out)
        final_out = re.sub(r'\*.', '', final_out)
        final_out = re.sub(r'-. ', '', final_out)
        final_out = re.sub(r'-.', '', final_out)
        #final_out = re.sub(r'\**.\* ', '', final_out)
        #final_out = re.sub(r'\**.\*', '', final_out)
        final_out = re.sub(r'\*{,3}.\*.. ', '', final_out)
        final_out = re.sub(r'\*{,3}.\*. ', '', final_out)
        final_out = re.sub(r'\*.. ', '', final_out)
        final_out = re.sub(r'\*..', '', final_out)
        final_out = re.sub(r'\* ', '', final_out)
        #final_out = re.sub(r'\*', '', final_out)
        final_out = re.sub(r'- ', '', final_out)
        final_out = re.sub(r'-', '', final_out)
        final_out = re.sub(r'; ; ', '; ', final_out)
        final_out = final_out[:-1]
        ptb_sent_file.write(final_out)
        ptb_sent_file.write("\n")
        #print(final_out)
        count+=1
        #if count == 10000: break
        #if count > 10: break
    ptb_sent_file.close()
    print(count)

CorpusPTBReader("./parsed/mrg/")
