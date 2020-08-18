#!/usr/bin/env python3

"""
extract.py
-----
python extract.py input_file.pdf output_file.json

Extract PDF sections into JSON
"""

import sys
import json
import collections
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from transformers import BertTokenizer
from pdfir.Retrieval import InvertedIndex


def CalculateTermFrequency(text):
    # convert text to tokens
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    tokens = tokenizer.tokenize(text)

    # each unique token is a term
    terms = collections.Counter(tokens)

    return terms



"""
Inputs
"""
input_file = sys.argv[1]
output_file = sys.argv[2]


if(output_file.split('.')[1] != 'json'):
    print("Output file must be json.")
    exit()




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

    print("Parsed : ", page_no)



# write to file
data = VocabularyIndex.get_index()
with open(output_file, 'w') as f:
    json.dump(data, f, ensure_ascii=False)