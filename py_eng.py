# -*- coding: utf-8 -*- 
from google_trans_new import google_translator  
import os,re

path = os.path.abspath(os.curdir) + '\\'
print(path)

translator = google_translator()  

def translate(text,translator):
    translate_text = translator.translate(text, lang_src='en', lang_tgt='ru')  
    return translate_text

with open(path + 'text.txt','r', encoding='utf8') as handle:
    lines = handle.readlines()
    flag = 1
    ori_text = ''
    dest_text = []
    common_dict = {}
    for line in lines:
        if line != '':
            line = line.replace('\n','').replace('»','').replace('«','')
            words = re.sub('[_]|[.]|[,]|[\d]|[)]','',line).split(' ')
            for word in words:
                common_dict[word]=translate(word,translator)
            if ')' in line:
                if flag == 1:
                    result_text = translate(dest_text,translator)
                    print(ori_text,result_text)
                    dest_text = []
                    flag=0
                ori_text = line
                
            else:
                dest_text.append(line)
                dest_text.append(ori_text.replace('_____',line))
                flag=1
with open(path + 'dict.csv','w') as handle_out:
    for a in common_dict:
        handle_out.write('\n'+ a + ';' + common_dict[a])
print(common_dict)
