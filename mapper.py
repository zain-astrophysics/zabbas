#!/usr/bin/env python

import sys
import re
import string
import requests
import os
import tarfile
speeches = []


# Load stopwords
stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
stopwords = list(set(stopwords_list.decode().splitlines()))


def calc_valence(text):
    TEXT = text.split()
    word_valences = []
    print(TEXT)
    for word_split in TEXT:
        print(word_split)
        word_val = afinn.get(word_split, 0)
        word_valences.append((word_split, word_val))
    return word_valences

#  it takes a line of any presidential speech and returns its valence after cleaning it
def valence(text):
   
    return calc_valence(clean_text(text))



# Load AFINN-165 lexicon (you should download it from an external source or ensure it's available)
def load_afinn():
    url = "https://raw.githubusercontent.com/fnielsen/afinn/master/afinn/data/AFINN-en-165.txt"
    response = requests.get(url)
    data = response.text
    afinn = {}
    for line in data.splitlines():
        word, score = line.split('\t')
        afinn[word] = int(score)
    return afinn
    
# Load the AFINN-165 sentiment lexicon
afinn = load_afinn()

# Function to remove stopwords from a given text
def remove_stopwords(text):
    return [word for word in text.split() if word not in stopwords]


# Function to clean text (remove punctuation, digits, stopwords)
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\[.*?\]', '', text)  # Remove anything in square brackets
    text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)  # Remove punctuation
    text = re.sub(r'[\d]+', ' ', text)  # Remove numbers
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.strip()
    return ' '.join(remove_stopwords(text))

# Mapper function
def mapper(argv):
    #president_name = os.environ['mapreduce_map_input_file'] #*****
    president_name = 'adams'
    for line in sys.stdin.readline():
        word_valences = valence(line)
        for word, word_valence in word_valences:
            print(f"{president_name}\t{word_valence}")
            

# This would be invoked by the Hadoop job framework
if __name__ == "__main__":
    mapper(sys.argv)
