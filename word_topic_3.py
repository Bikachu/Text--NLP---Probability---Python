# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 03:45:10 2018

@author: PeterLi
"""


import pandas as pd
import numpy as np 
import csv
import nltk
import collections
from collections import Counter


with open('words_and_topics.tsv','rt',encoding='utf-8') as data:
    dataset = csv.reader(data, delimiter='\t')
    filecontents = [line for line in dataset]
    dataset = pd.DataFrame(filecontents)
    dataset.columns = ['word', 'topic']
    
    
    #add a additional column for counting and get rid of the repeated lines
    df = dataset.groupby(dataset.columns.tolist()).size().reset_index().rename(columns={0:'count'})
    
    
    # get rid of the repated word in df
    distinct_words = nltk.FreqDist(df['word'])
    
    #sample = {key.lower(): value for key, value in distinct_words.items()}

from functools import reduce   
row = []
for key_1 in distinct_words.keys():
    
    for key_2 in distinct_words.keys():
        
        if  key_1 != key_2 and key_1.lower() ==key_2.lower():
            #print(key_1, key_2)
            topic1 =df['topic'][df['word']==key_1]
            topic2 =df['topic'][df['word']==key_2]
            number = len(set(topic1) - set(topic2))
            row.append(number)
print(reduce(lambda x, y: x + y, row) / len(row))
    
#the result is 9.160046342270771
     



        
        
        
        
        
        
        
        
    
   