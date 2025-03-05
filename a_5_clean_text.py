#!/usr/bin/env python

import requests, re, string

# Retrieve the list of stopwords
stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
stopwords = list(set(stopwords_list.decode().splitlines()))

def remove_stopwords(words):
    # Remove non-alphanumeric characters and split the words
    list_ = re.sub(r'[^a-zA-Z0-9]', " ", words.lower()).split()
    # Return only the words that are not in stopwords
    return [itm for itm in list_ if itm not in stopwords]

def ο(text, prev_text=""):
    # Check: if the text hasn't changed after cleaning, stop recursion

    if text == prev_text:
        return text


    #Step 1: lower the capital words
    text = text.lower()


    # Step 2: Remove content inside square brackets
    text = re.sub(r'\[.*?\]', '', text)
    
    # Step 3: Remove punctuation and numbers
    text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub(r'[\d]+', ' ', text)

    # Step 4: Remove stopwords
    words = remove_stopwords(text)

    # Step 5: Join the words and apply recursion with the cleaned text
    cleaned_text = ' '.join(words)
    
    # Recursively clean the text until no further changes occur
    return ο(cleaned_text, prev_text=text)

# Example 
#text = "A very long and messy string with [extra] words, punctuation, and numbers like 1234."
#cleaned_text = ο(text)
#print(cleaned_text)