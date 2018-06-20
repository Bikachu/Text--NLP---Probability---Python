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
    
    
#problem 1: The total length of the data 
    print("The total length of the dataset is :"+ str(len(dataset)))
    
# problem 2: The 10 most common lines:
    lines = ["for-enterainment", "for-sports", "Award-entertainment", "Shorty-entertainment","nominate-entertainment","in-sports", "a-sports", "I-sports", "Pets-ebc", "eBC-pets"]
    print('\n')
    print("The 10 most common lines are :" + str(lines))
    print('\n')
    

# problem 3: the 10 most common topics
    print('\n')
    print("The 10 most common topics:" + str(dataset_topic.most_common(10)))
    print('\n')
    
# problem 4: The 10 most common words
    print('\n')
    print("The 10 most common words:" + str(dataset_words.most_common(10)))
    print('\n')
    
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
    
for element in topic_10:
    
    words_topic = dataset.loc[dataset['topic'] ==element, 'word']
    word_10 = [word[0] for word in nltk.FreqDist(words_topic).most_common(10)]
    print("The 10 most common word for topic"+ " " + element  + " " + "is" + str(word_10))
          

#The 10 most common word for topic health is['to', 'loss', 'Weight', 'the', 'for', 'weight', 'of', 'The', 'natural', 'Loss']
#The 10 most common word for topic sports is['for', 'in', 'a', 'I', 'the', 'nominate', 'Shorty', 'Award', 'because', 'to']
#The 10 most common word for topic technology is['for', 'new', 'CES', 'with', 'the', 'and', 'to', 'BRK', 'at', 'Android']
#The 10 most common word for topic politics is['in', 'a', 'for', 'Award', 'Shorty', 'nominate', 'the', 'to', 'because', 'of']
#The 10 most common word for topic entertainment is['for', 'Shorty', 'Award', 'nominate', 'because', 'is', 'the', 'and', 'he', 'of']
#The 10 most common word for topic news is['Sports', 'to', 'health', 'sports', 'the', 'in', 'The', 'of', 'for', 'politics']
#The 10 most common word for topic pets is['eBC', 'animals', 'craigslist', 'SFO', 'dogs', 'Please', 'Contact', 'home', 'puppies', 'for']
#The 10 most common word for topic science is['a', 'in', 'for', 'Shorty', 'Award', 'nominate', 'because', 'the', 'of', 'to']
#The 10 most common word for topic finance is['Jobs', 'Job', 'TweetMyJOBS', 'the', 'to', 'for', 'Financial', 'Business', 'Citigroup', 'Management']
#The 10 most common word for topic ebc is['Pets', 'Please', 'Contact', 'puppies', 'Miami', 'old', 'Puppy', 'AKC', 'Chicago', '$200']



         

#probability of a topic given word     
def prob(word_input,topic_input):
    
    topic_numb = word_count[word_input]
    
    
    topic_re_numb =df['count'][(df['topic']== topic_input )&(df['word']==word_input)]
    prob = topic_re_numb/topic_numb
    print("The probability of topic " + topic_input  +" is: " + str(list(prob)[0])+" given a input word " + word_input)

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
word_2 = ['for', 'in', 'a', 'I', 'the', 'nominate', 'Shorty','Award', 'because', 'to']
word_3 = ['for', 'new', 'CES', 'with', 'the', 'and', 'to', 'BRK', 'at', 'Android']
word_4 = ['in','a','for','Award','Shorty','nominate','the','to','because','of']
word_5 = ['for', 'Shorty', 'Award', 'nominate', 'because', 'is', 'the', 'and', 'he', 'of']
word_6 = ['Sports', 'to', 'health', 'sports', 'the', 'in', 'The', 'of', 'for', 'politics']
word_7 = ['eBC', 'animals', 'craigslist', 'SFO', 'dogs', 'Please', 'Contact', 'home', 'puppies', 'for']
word_8 = ['a', 'in', 'for', 'Shorty', 'Award', 'nominate', 'because', 'the', 'of', 'to']
word_9 = ['Jobs', 'Job', 'TweetMyJOBS', 'the', 'to', 'for', 'Financial', 'Business', 'Citigroup', 'Management']
word_10 = ['Pets', 'Please', 'Contact', 'puppies', 'Miami', 'old', 'Puppy', 'AKC', 'Chicago', '$200']

#probability for health:

    
for word in word_1:
    prob(word, 'health')
    
#The probability of topic health is: 0.10999083409715857 given a input word to
#The probability of topic health is: 0.18822553897180763 given a input word loss
#The probability of topic health is: 0.22945205479452055 given a input word Weight
#The probability of topic health is: 0.07717041800643087 given a input word the
#The probability of topic health is: 0.060125414976023604 given a input word for
#The probability of topic health is: 0.23600605143721634 given a input word weight
#The probability of topic health is: 0.1028533510285335 given a input word of
#The probability of topic health is: 0.10717100078802207 given a input word The
#The probability of topic health is: 0.21634615384615385 given a input word natural
#The probability of topic health is: 0.21649484536082475 given a input word Loss
    


for word in word_2:
    prob(word, 'sports')
    
#The probability of topic sports is: 0.1431206196975286 given a input word for
#The probability of topic sports is: 0.2072480181200453 given a input word in
#The probability of topic sports is: 0.3031634446397188 given a input word a
#The probability of topic sports is: 0.6888888888888889 given a input word I
#The probability of topic sports is: 0.1382636655948553 given a input word the
#The probability of topic sports is: 0.28720083246618106 given a input word nominate
#The probability of topic sports is: 0.2781799379524302 given a input word Shorty
#The probability of topic sports is: 0.2774327122153209 given a input word Award
#The probability of topic sports is: 0.28174123337363965 given a input word because
#The probability of topic sports is: 0.0930339138405133 given a input word to




for word in word_3:
    prob(word,'technology')

#The probability of topic technology is: 0.06934710438952416 given a input word for
#The probability of topic technology is: 0.2587800369685767 given a input word new
#The probability of topic technology is: 0.34366925064599485 given a input word CES
#The probability of topic technology is: 0.1495433789954338 given a input word with
#The probability of topic technology is: 0.05236564079007809 given a input word the
#The probability of topic technology is: 0.09739130434782609 given a input word and
#The probability of topic technology is: 0.04995417048579285 given a input word to
#The probability of topic technology is: 0.7322834645669292 given a input word BRK
#The probability of topic technology is: 0.13509544787077826 given a input word at
#The probability of topic technology is: 0.2793103448275862 given a input word Android
    



for word in word_4:
    prob(word,'politics')

#The probability of topic politics is: 0.11891279728199321 given a input word in
#The probability of topic politics is: 0.18189806678383127 given a input word a
#The probability of topic politics is: 0.11891279728199321 given a input word in
#The probability of topic politics is: 0.13664596273291926 given a input word Award
#The probability of topic politics is: 0.13547052740434332 given a input word Shorty
#The probability of topic politics is: 0.13527575442247658 given a input word nominate
#The probability of topic politics is: 0.0532843362425356 given a input word the
#The probability of topic politics is: 0.04903758020164986 given a input word to
#The probability of topic politics is: 0.12212817412333736 given a input word because
#The probability of topic politics is: 0.06104844061048441 given a input word of
    
    


for word in word_5:
    
    prob(word,'entertainment')

#The probability of topic entertainment is: 0.1563998524529694 given a input word for
#The probability of topic entertainment is: 0.3929679420889349 given a input word Shorty
#The probability of topic entertainment is: 0.39337474120082816 given a input word Award
#The probability of topic entertainment is: 0.3891779396462019 given a input word nominate
#The probability of topic entertainment is: 0.37001209189842804 given a input word because
#The probability of topic entertainment is: 0.1361111111111111 given a input word is
#The probability of topic entertainment is: 0.044097381717960495 given a input word the
#The probability of topic entertainment is: 0.05391304347826087 given a input word and
#The probability of topic entertainment is: 0.26344086021505375 given a input word he
#The probability of topic entertainment is: 0.03185136031851361 given a input word of
            


for word in word_6:
    prob(word, 'news')

#The probability of topic news is: 0.19337979094076654 given a input word Sports
#The probability of topic news is: 0.043996333638863426 given a input word to
#The probability of topic news is: 0.025423728813559324 given a input word health
#The probability of topic news is: 0.05508474576271186 given a input word sports
#The probability of topic news is: 0.02756086357372531 given a input word the
#The probability of topic news is: 0.03001132502831257 given a input word in
#The probability of topic news is: 0.04097714736012608 given a input word The
#The probability of topic news is: 0.0325149303251493 given a input word of
#The probability of topic news is: 0.016230173367760975 given a input word for
#The probability of topic news is: 0.08102766798418973 given a input word politics   
    
            

for word in word_7:
    
    prob(word,'pets')
    
#The probability of topic pets is: 1.0 given a input word eBC
#The probability of topic pets is: 0.31004366812227074 given a input word animals
#The probability of topic pets is: 0.2397003745318352 given a input word craigslist
#The probability of topic pets is: 0.26666666666666666 given a input word SFO
#The probability of topic pets is: 0.1856060606060606 given a input word dogs
#The probability of topic pets is: 0.4067796610169492 given a input word Please
#The probability of topic pets is: 0.4528301886792453 given a input word Contact
#The probability of topic pets is: 0.11363636363636363 given a input word home
#The probability of topic pets is: 0.35398230088495575 given a input word puppies
#The probability of topic pets is: 0.012910365178900774 given a input word for
     
    

for word in word_8:
    
    prob(word,'science')
 
#The probability of topic science is: 0.16520210896309315 given a input word a
#The probability of topic science is: 0.09796149490373726 given a input word in
#The probability of topic science is: 0.052010328292143124 given a input word for
#The probability of topic science is: 0.1313340227507756 given a input word Shorty
#The probability of topic science is: 0.13146997929606624 given a input word Award
#The probability of topic science is: 0.13111342351716962 given a input word nominate
#The probability of topic science is: 0.12333736396614269 given a input word because
#The probability of topic science is: 0.04455672944418925 given a input word the
#The probability of topic science is: 0.05242203052422031 given a input word of
#The probability of topic science is: 0.03162236480293309 given a input word to

    
            


for word in word_9:
    prob(word,'finance')

#The probability of topic finance is: 0.2687813021702838 given a input word Jobs
#The probability of topic finance is: 0.3557692307692308 given a input word Job
#The probability of topic finance is: 0.20995670995670995 given a input word TweetMyJOBS
#The probability of topic finance is: 0.024345429490124023 given a input word the
#The probability of topic finance is: 0.022456461961503207 given a input word to
#The probability of topic finance is: 0.016599040944300997 given a input word for
#The probability of topic finance is: 0.19736842105263158 given a input word Financial
#The probability of topic finance is: 0.15172413793103448 given a input word Business
#The probability of topic finance is: 0.18777292576419213 given a input word Citigroup
#The probability of topic finance is: 0.23243243243243245 given a input word Management
            
    

 
for word in word_10:
    prob(word,'ebc')    
    
#The probability of topic ebc is: 0.9279279279279279 given a input word Pets
#The probability of topic ebc is: 0.4067796610169492 given a input word Please
#The probability of topic ebc is: 0.4528301886792453 given a input word Contact
#The probability of topic ebc is: 0.2831858407079646 given a input word puppies
#The probability of topic ebc is: 0.4307692307692308 given a input word Miami
#The probability of topic ebc is: 0.4166666666666667 given a input word old
#The probability of topic ebc is: 0.46153846153846156 given a input word Puppy
#The probability of topic ebc is: 0.5 given a input word AKC
#The probability of topic ebc is: 0.21100917431192662 given a input word Chicago
#The probability of topic ebc is: 0.5 given a input word $200
    