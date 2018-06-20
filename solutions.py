# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:59:47 2018

@author: PeterLi
"""

import pandas as pd
import numpy as np 
import csv
import nltk

with open('words_and_topics.tsv','rt',encoding='utf-8') as data:
    dataset = csv.reader(data, delimiter='\t')
    filecontents = [line for line in dataset]
    dataset = pd.DataFrame(filecontents)
    
    
    #problem 1
    print(len(dataset))
    
    dataset_topic = nltk.FreqDist(dataset[1])
    dataset_words = nltk.FreqDist(dataset[0])
    
    
    # Problem 3
    print("The 10 most common topics:" + str(dataset_topic.most_common(10)))
    
    #Problem 4
    print("The 10 most common words:" + str(dataset_words.most_common(10)))
    
    #problem 5
    dataset_topic_10 = dataset_topic.most_common(10)
    topic_10 = [topic[0] for topic in dataset_topic_10]
    
    #  [('health', 15697), 
    #  ('sports', 12840),
    #  ('technology', 8221), 
    #   ('politics', 6323), 
    #   ('entertainment', 6001), 
    #   ('news', 5306), 
    #  ('pets', 4977), 
    #  ('science', 4861), 
    #  ('finance', 4218), 
    #  ('ebc', 3029)]
    
            
    for topic in dataset[1]:
        
        if topic == "health":
            words_health = dataset.loc[dataset[1] ==topic, 0]
            health_10 = [word[0] for word in nltk.FreqDist(words_health).most_common(10)]
    # ['to', 'loss', 'Weight', 'the', 'for', 'weight', 'of', 'The', 'natural', 'Loss']
    
    
    for topic in dataset[1]:
        
        if topic == "sports":
            words_sports = dataset.loc[dataset[1] ==topic, 0]
            sports_10 = [word[0] for word in nltk.FreqDist(words_sports).most_common(10)]
    #['for', 'in', 'a', , 'I', 'the', 'nominate', 'Shorty','Award', 'because', 'to']
            
    
            
    for topic in dataset[1]:
        
        if topic == "technology":
            words_technology = dataset.loc[dataset[1] ==topic, 0]
            technology_10 = [word[0] for word in nltk.FreqDist(words_technology).most_common(10)]
           # print(technology_10)
    # ['for', 'new', 'CES', 'with', 'the', 'and', 'to', 'BRK', 'at', 'Android']
            
           
    for topic in dataset[1]:
        
        if topic == "politics":
            words_politics = dataset.loc[dataset[1] ==topic, 0]
            politics_10 = [word[0] for word in nltk.FreqDist(words_politics).most_common(10)]
            # print(politics_10)
    # ['in','a','for','Award','Shorty','nominate','the','to','because','of']
    
            
    for topic in dataset[1]:
        
        if topic == "entertainment":
            words_entertainment = dataset.loc[dataset[1] ==topic, 0]
            entertainment_10 = [word[0] for word in nltk.FreqDist(words_entertainment).most_common(10)]
            # print(entertainment_10)
    # ['for', 'Shorty', 'Award', 'nominate', 'because', 'is', 'the', 'and', 'he', 'of']
    
            
    for topic in dataset[1]:
        
        if topic == "news":
            words_news = dataset.loc[dataset[1] ==topic, 0]
            news_10 = [word[0] for word in nltk.FreqDist(words_news).most_common(10)]
            #print(news_10)
    # ['Sports', 'to', 'health', 'sports', 'the', 'in', 'The', 'of', 'for', 'politics']
    
            
    for topic in dataset[1]:
        
        if topic == "pets":
            words_pets = dataset.loc[dataset[1] ==topic, 0]
            pets_10 = [word[0] for word in nltk.FreqDist(words_pets).most_common(10)]
            #print(pets_10)
    # ['eBC', 'animals', 'craigslist', 'SFO', 'dogs', 'Please', 'Contact', 'home', 'puppies', 'for']
     
      
    for topic in dataset[1]:
        
        if topic == "science":
            words_science = dataset.loc[dataset[1] ==topic, 0]
            science_10 = [word[0] for word in nltk.FreqDist(words_science).most_common(10)]
            #print(science_10)
    # ['a', 'in', 'for', 'Shorty', 'Award', 'nominate', 'because', 'the', 'of', 'to']
    
            
    for topic in dataset[1]:
        
        if topic == "finance":
            words_finance = dataset.loc[dataset[1] ==topic, 0]
            finance_10 = [word[0] for word in nltk.FreqDist(words_finance).most_common(10)]
            #print(finance_10)
    # ['Jobs', 'Job', 'TweetMyJOBS', 'the', 'to', 'for', 'Financial', 'Business', 'Citigroup', 'Management']
            
    
    for topic in dataset[1]:
        
        if topic == "ebc":
            words_ebc = dataset.loc[dataset[1] ==topic, 0]
            ebc_10 = [word[0] for word in nltk.FreqDist(words_ebc).most_common(10)]
            #print(ebc_10)
    # ['Pets', 'Please', 'Contact', 'puppies', 'Miami', 'old', 'Puppy', 'AKC', 'Chicago', '$200']
        
    
    

   # problem 6     
        
        
        
        
   # problem 10
   #dataset_freq = nltk.FreqDist(dataset)
            
            
    
    
    