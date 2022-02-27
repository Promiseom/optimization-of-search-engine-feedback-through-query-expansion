# author: anendahpromise@gmail.com
# date: September, 2021
# Query Expansion implementation using Relevance Feedback with Wordnet

import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem import WordNetLemmatizer
from nltk.wsd import lesk
import sys

def transform_sentence(sentence):
    ''' Takes a sentence and transforms the input string. At the basic level, converts the input string to lowercase '''
    return sentence.lower()

def tokenize_sentence(sentence):
    ''' Breaks a sentence into terms - individual words that make up the sentence. '''
    return word_tokenize(sentence)

def eliminate_stopwords(tokens):
    ''' Takes a list of tokens and removes all the stopwords from the list of tokens. '''
    words = stopwords.words('english')
    result = [token for token in tokens if token not in words]
    return result

# The tag mapping of for tag conversion from nltk tags to wordnet tags
pos_tag_map = {
    'NN': [ wordnet.NOUN ],
    'JJ': [ wordnet.ADJ_SAT ],
    'RB': [ wordnet.ADV ],
    'VB': [ wordnet.VERB ]
}

def pos_tag_converter(nltk_pos_tag):
    ''' Converts an NLTK tag to wordnet usable format. '''
    root_tag = nltk_pos_tag[0:2]
    try:
        pos_tag_map[root_tag]
        return pos_tag_map[root_tag]
    except KeyError:
        return ''

def lemmatize_terms(tokens):
    ''' Takes a list of terms and returns the basic form of the words. '''
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def attach_pos_tag(tokens):
    ''' Takes a list of tokens add part of speech to the tokens. '''
    return nltk.pos_tag(tokens)

def convert_token_tags(tokens):
    ''' Takes tokens and converts tags that can be used by Wordnet. '''
    result = []
    for token in tokens:
        tag = pos_tag_converter(token[1])
        if(tag == ''): raise Exception('Invalid tag found!')
        result.append([token[0], tag])
    return result

def process_string(sentence):
    sentence = transform_sentence(sentence)
    tokens = tokenize_sentence(sentence)
    tokens = eliminate_stopwords(tokens)
    tokens = lemmatize_terms(tokens)
    return output

def get_wordnet_senses(token):
    ''' Receives a token and returns the word senses of the specified token. '''
    return wordnet.synsets(token[0], token[1][0])

def get_synonyms(word):
	''' Returns a list of synonyms of a particular word'''
	word_senses = wordnet.synsets(word)
	synonyms = []
	if len(word_senses) < 1: return synonyms
	sense = word_senses[0]
	for i in sense.lemmas():
		if i.name() not in synonyms: synonyms.append(i.name().lower())

	for hyp in sense.hypernyms():
		synonyms += [x.name() for x in hyp.lemmas()]
	#remove duplicates
	return list(set(synonyms))

def get_query_synonyms(q_terms):
    synonyms = []
    for term in q_terms.split():
        synonyms += get_synonyms(term)
    return synonyms

def disambiguate(word, context):
    return lesk(context, word)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        q_terms = sys.argv[1]
    else: q_terms = 'programming language'
    print('Synonyms of', q_terms)
    for syn in get_query_synonyms(q_terms):
        print(syn)
    print()
