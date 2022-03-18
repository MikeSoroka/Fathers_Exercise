import sys
import os

cin = open('Alice.txt', 'r')
cout = open('stdout.txt', 'w')

def text_mod(content):
    text = content.translate(str.maketrans("", "", '".?!,:;`()[]_')).replace("- ", "").replace(" '", "").replace("' ", "").replace("',", "").replace("'.", "").replace("'!", "").replace("'?", "")
    text = sorted(text.lower().split())

    word_counter = {}
    for i in text:
        word_counter[i] = word_counter.get(i, 0) + 1

    sorted_word_counter = {}
    keys_list = sorted(word_counter, key = word_counter.get)
    for w in keys_list:
        sorted_word_counter[w] = word_counter[w]
 
    return sorted_word_counter


def max_length(arr):
    lengths = []
    for i in arr:
        lengths.append(len(i))
        #cout.write(str(i) + " ")
    return max(lengths)


def write_dict(dictionary):
    l = max_length(list(dictionary.keys()))
    for i in dictionary:
        cout.write(i + " " * (l - len(i)) + ": " + str(dictionary[i]) + "\n")


#os.system('chmod +x words_counter.py')
#os.system('!/usr/bin/env python')
#os.system('mv words_counter.py words_counter')
#os.system('mkdir -p ~/bin')
#os.system('cp square ~/bin')
#os.system('export PATH=$PATH":$HOME/bin"')

#file = sys.argv[1]
content = cin.read()

content_mod = text_mod(content)
write_dict(content_mod)

cin.close()
cout.close()