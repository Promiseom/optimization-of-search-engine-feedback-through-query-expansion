# Handles the selection of query expansion terms from a list of 
# Candidate Expansion terms from Wikipedia

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class TermSelector:
    def __init__(self):
        self.__expansion_terms = []


    def refine_terms(self, raw_terms, original_query):
        refined_terms = []
        all_terms = []        
        bad_words = stopwords.words('english')
        q_t = word_tokenize(original_query)

        for term in raw_terms:
            tmp = ""
            term = term.lower()
            t = word_tokenize(term)
            # remove the stop words and words that already occur
            t = [i for i in t if i not in bad_words and i not in all_terms]
            # remove words already in the original query
            t = [i for i in t if i not in q_t]
            t = [i for i in t if i.isalnum() or i == ' ']

            for s in t:
                tmp += s + ' '
            tmp.strip()
            if(len(tmp) > 0): refined_terms.append(tmp)
            all_terms += t
        return [refined_terms, all_terms]






