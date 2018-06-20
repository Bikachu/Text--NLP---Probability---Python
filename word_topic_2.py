
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 04:38:56 2018

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
    dataset.columns = ['word', 'topic']
    
    
    
    dataset_topic = nltk.FreqDist(dataset['topic'])
    dataset_words = nltk.FreqDist(dataset['word'])
    
    
    #add a additional column for counting the repeated lines
    df = dataset.groupby(dataset.columns.tolist()).size().reset_index().rename(columns={0:'count'})

    
    topic_count = dataset['topic'].value_counts()
    word_count = dataset['word'].value_counts()
    
    
    topic_count['actuary']
    e=df['count'][(df['topic']=='actuary')&(df['word']=='Jobs')]
    prob = e/topic_count['actuary']
    list(prob)[0]
   
 

#probability of a word given topic    
def prob(word_input,topic_input):
    
    #total number of words of a given topic 
    word_numb = topic_count[topic_input]
    
    #number of repeated given word for a given topic
    word_re_numb =df['count'][(df['topic']== topic_input )&(df['word']==word_input)]
    
    #The probability
    prob = word_re_numb/word_numb
    
    print("The probability of word " + word_input  +" is: " + str(list(prob)[0])+" given a input topic " + topic_input)

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
        
        
        
word_1 = ['to', 'loss', 'Weight', 'the', 'for', 'weight', 'of', 'The', 'natural', 'Loss']
#probability for health:

for word in word_1:
    prob(word, 'health')
    
#The probability of word to is: 0.015289545773077657 given a input topic health
#The probability of word loss is: 0.014461362043702618 given a input topic health
#The probability of word Weight is: 0.012804994584952538 given a input topic health
#The probability of word the is: 0.010702682041154361 given a input topic health
#The probability of word for is: 0.010384149837548576 given a input topic health
#The probability of word weight is: 0.009938204752500478 given a input topic health
#The probability of word of is: 0.00987449831177932 given a input topic health
#The probability of word The is: 0.00866407593807734 given a input topic health
#The probability of word natural is: 0.008600369497356182 given a input topic health
#The probability of word Loss is: 0.00802701153086577 given a input topic health

word_2 = ['for', 'in', 'a', 'I', 'the', 'nominate', 'Shorty','Award', 'because', 'to']

for word in word_2:
    prob(word, 'sports')
    
#The probability of word for is: 0.030218068535825544 given a input topic sports
#The probability of word in is: 0.02850467289719626 given a input topic sports
#The probability of word a is: 0.026869158878504672 given a input topic sports
#The probability of word I is: 0.024143302180685357 given a input topic sports
#The probability of word the is: 0.023442367601246107 given a input topic sports
#The probability of word nominate is: 0.02149532710280374 given a input topic sports
#The probability of word Shorty is: 0.020950155763239876 given a input topic sports
#The probability of word Award is: 0.020872274143302182 given a input topic sports
#The probability of word because is: 0.018146417445482867 given a input topic sports
#The probability of word to is: 0.015809968847352026 given a input topic sports


word_3 = ['for', 'new', 'CES', 'with', 'the', 'and', 'to', 'BRK', 'at', 'Android']

for word in word_3:
    prob(word,'technology')

#The probability of word for is: 0.022868264201435347 given a input topic technology
#The probability of word new is: 0.017029558447877388 given a input topic technology
#The probability of word CES is: 0.01617808052548352 given a input topic technology
#The probability of word with is: 0.015934801119085268 given a input topic technology
#The probability of word the is: 0.013866926164700158 given a input topic technology
#The probability of word and is: 0.01362364675830191 given a input topic technology
#The probability of word to is: 0.013258727648704538 given a input topic technology
#The probability of word BRK is: 0.01131249239751855 given a input topic technology
#The probability of word at is: 0.011190852694319426 given a input topic technology
#The probability of word Android is: 0.00985281595912906 given a input topic technology
    

word_4 = ['in','a','for','Award','Shorty','nominate','the','to','because','of']

for word in word_4:
    prob(word,'politics')

#The probability of word in is: 0.033212082872054405 given a input topic politics
#The probability of word a is: 0.03273762454531077 given a input topic politics
#The probability of word for is: 0.028783805155780485 given a input topic politics
#The probability of word Award is: 0.02087616637671991 given a input topic politics
#The probability of word Shorty is: 0.0207180136011387 given a input topic politics
#The probability of word nominate is: 0.02055986082555749 given a input topic politics
#The probability of word the is: 0.018345721967420528 given a input topic politics
#The probability of word to is: 0.016922346987189626 given a input topic politics
#The probability of word because is: 0.015973430333702358 given a input topic politics
#The probability of word of is: 0.014550055353471453 given a input topic politics
    
    
word_5 = ['for', 'Shorty', 'Award', 'nominate', 'because', 'is', 'the', 'and', 'he', 'of']

for word in word_5:
    
    prob(word,'entertainment')

#The probability of word for is: 0.07065489085152475 given a input topic entertainment
#The probability of word Shorty is: 0.06332277953674388 given a input topic entertainment
#The probability of word Award is: 0.06332277953674388 given a input topic entertainment
#The probability of word nominate is: 0.06232294617563739 given a input topic entertainment
#The probability of word because is: 0.05099150141643059 given a input topic entertainment
#The probability of word is is: 0.01633061156473921 given a input topic entertainment
#The probability of word the is: 0.015997333777703716 given a input topic entertainment
#The probability of word and is: 0.010331611398100316 given a input topic entertainment
#The probability of word he is: 0.008165305782369604 given a input topic entertainment
#The probability of word of is: 0.007998666888851858 given a input topic entertainment
            
word_6 = ['Sports', 'to', 'health', 'sports', 'the', 'in', 'The', 'of', 'for', 'politics']

for word in word_6:
    prob(word, 'news')

#The probability of word Sports is: 0.020919713531850737 given a input topic news
#The probability of word to is: 0.018092725216735772 given a input topic news
#The probability of word health is: 0.012438748586505842 given a input topic news
#The probability of word sports is: 0.012250282698831511 given a input topic news
#The probability of word the is: 0.011307953260459858 given a input topic news
#The probability of word in is: 0.00998869204673954 given a input topic news
#The probability of word The is: 0.00980022615906521 given a input topic news
#The probability of word of is: 0.009234828496042216 given a input topic news
#The probability of word for is: 0.008292499057670561 given a input topic news
#The probability of word politics is: 0.007727101394647569 given a input topic news
    
            
word_7 = ['eBC', 'animals', 'craigslist', 'SFO', 'dogs', 'Please', 'Contact', 'home', 'puppies', 'for']
for word in word_7:
    
    prob(word,'pets')
    
#The probability of word eBC is: 0.062085593731163354 given a input topic pets
#The probability of word animals is: 0.01426562186055857 given a input topic pets
#The probability of word craigslist is: 0.01285915209965843 given a input topic pets
#The probability of word SFO is: 0.01285915209965843 given a input topic pets
#The probability of word dogs is: 0.009845288326300985 given a input topic pets
#The probability of word Please is: 0.009644364074743821 given a input topic pets
#The probability of word Contact is: 0.009644364074743821 given a input topic pets
#The probability of word home is: 0.008036970062286517 given a input topic pets
#The probability of word puppies is: 0.008036970062286517 given a input topic pets
#The probability of word for is: 0.007032348804500703 given a input topic pets
     
    
word_8 = ['a', 'in', 'for', 'Shorty', 'Award', 'nominate', 'because', 'the', 'of', 'to']
for word in word_8:
    
    prob(word,'science')
 
#The probability of word a is: 0.03867516971816499 given a input topic science
#The probability of word in is: 0.03558938490022629 given a input topic science
#The probability of word for is: 0.02900637728862374 given a input topic science
#The probability of word Shorty is: 0.026126311458547623 given a input topic science
#The probability of word Award is: 0.026126311458547623 given a input topic science
#The probability of word nominate is: 0.025920592470685046 given a input topic science
#The probability of word because is: 0.02098333676198313 given a input topic science
#The probability of word the is: 0.019954741822670232 given a input topic science
#The probability of word of is: 0.016251800041143797 given a input topic science
#The probability of word to is: 0.014194610162518 given a input topic science
    
            
word_9 = ['Jobs', 'Job', 'TweetMyJOBS', 'the', 'to', 'for', 'Financial', 'Business', 'Citigroup', 'Management']

for word in word_9:
    prob(word,'finance')

#The probability of word Jobs is: 0.03816974869606449 given a input topic finance
#The probability of word Job is: 0.03508771929824561 given a input topic finance
#The probability of word TweetMyJOBS is: 0.022996680891417733 given a input topic finance
#The probability of word the is: 0.012565196775723092 given a input topic finance
#The probability of word to is: 0.011616880037932669 given a input topic finance
#The probability of word for is: 0.010668563300142247 given a input topic finance
#The probability of word Financial is: 0.010668563300142247 given a input topic finance
#The probability of word Business is: 0.010431484115694643 given a input topic finance
#The probability of word Citigroup is: 0.010194404931247037 given a input topic finance
#The probability of word Management is: 0.010194404931247037 given a input topic finance
            
    
word_10 = ['Pets', 'Please', 'Contact', 'puppies', 'Miami', 'old', 'Puppy', 'AKC', 'Chicago', '$200']
 
for word in word_10:
    prob(word,'ebc')    
    
#The probability of word Pets is: 0.10201386596236382 given a input topic ebc
#The probability of word Please is: 0.015846814130075933 given a input topic ebc
#The probability of word Contact is: 0.015846814130075933 given a input topic ebc
#The probability of word puppies is: 0.010564542753383956 given a input topic ebc
#The probability of word Miami is: 0.00924397490921096 given a input topic ebc
#The probability of word old is: 0.008253549026081214 given a input topic ebc
#The probability of word Puppy is: 0.007923407065037967 given a input topic ebc
#The probability of word AKC is: 0.0075932651039947174 given a input topic ebc
#The probability of word Chicago is: 0.0075932651039947174 given a input topic ebc
#The probability of word $200 is: 0.007263123142951469 given a input topic ebc