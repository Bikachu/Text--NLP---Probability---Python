# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 06:19:40 2018

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
    
    
    
    dataset_topic = nltk.FreqDist(dataset['topic'])
    dataset_words = nltk.FreqDist(dataset['word'])


    
    topic_count = dataset['topic'].value_counts()
    word_count = dataset['word'].value_counts()
    
    #add a additional column for counting and get rid of the repeated lines
    df = dataset.groupby(dataset.columns.tolist()).size().reset_index().rename(columns={0:'count'})
    
    df2 = df.sort_values(by='count', ascending=False)
    df3 = df2.reset_index(drop = True)
    
    
    
a = len(dataset)
 
numbers = []  

def precision(percent):
    
    for i in range (1,len(df3)):
        
        count = df3.loc[i-1,'count']
        numbers.append(count)
        
        if sum(numbers) >= a*percent:
            
            print(i)
            print(df3.loc[i-1,'count'])
            break

precision(0.9)
# 64175,  1

precision(0.95)
# 41,  136
    
precision(0.98)
# 19,  210    

#problem 10:

print(dataset_words)
    

    
    
    