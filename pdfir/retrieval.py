"""
retrieval.py
"""

import json
import collections
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from transformers import BertTokenizer


def ConstructInvertedIndex(input_file):
    """
    Construct an inverted index for a PDF file
    """
    
    VocabularyIndex = InvertedIndex()

    # iterate through document apges
    for page_layout in extract_pages(input_file):

        # compile all text on page
        page_text = ""
        for (count, element) in enumerate(page_layout, 1):
            if isinstance(element, LTTextContainer):
                page_text += element.get_text()

                
        # add page to inverted index
        page_no = int(page_layout.pageid)
        VocabularyIndex.index_document(page_no, page_text)


    data = VocabularyIndex.get_index()
    return data


class InvertedIndex:
    """
    Inverted Index class
    """
    def __init__(self):
        self.index = dict()

        
    def index_document(self, document_id, document):
        # convert text to term frequencies
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        tokens = tokenizer.tokenize(document)
        terms = collections.Counter(tokens)


        # add terms to inverted index
        for term, frequency in terms.items():
            update_dict = { term: {'frequency': frequency,
                                  'postings': [document_id]}
                            if term not in self.index
                            else {'frequency': self.index[term]['frequency'] + frequency,
                                  'postings': self.index[term]['postings'].append(document_id)}
                            }


        self.index.update(update_dict)

        return True


    def get_index(self):
        return self.index

    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances. 
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        return { term: self.index[term] for term in query.split(' ') if term in self.index }