# Text--NLP---Probability---Python

# Instructions:
=========================================================================================================== 
The input is a text file containing newline separated strings.

Each string is a word, followed by a tab, followed by a topic.


-----------------------------------------
#1. print the total number of lines.

#2. Print the 10 most common lines.

#3. Print the 10 most common topics, sorted by commonness.  A topic consists of the second part of each line, where each line is independent.

#4. Print the 10 most common words, sorted alphabetically.  A word consists of the first part of each line, where each line is independent.

#5. Print the 10 most common words for each of the top 10 most common topics.

#6. Write a function to compute the probability of a topic, given a word.  In your program, print this value for the 100 pairs of words and topics from #5.

#7. Write a function to compute the probability of a word, given a topic.  In your program, print this value for the 100 pairs of words and topics from #5.

#8. Write into your program a parameter that specifies whether the data should be treated case insensitively (treat "Apple" and "appLE" as the same), or case sensitively.

#9. Write into your program a parameter which specifies the minimum number of times a line must be seen to be considered.

#10. Print the frequency of each word count.  For example, there might be 68 words than occur 4 times, and 9 words that occur 8 times, and so on.


-----------------------
Solutions
-------------------------
word_topic1.py  includes: problem 1 - problem 6
word_topic2.py  includes problem 7
word_topic3.py  includes problem 8
word_topic4.py  includes problem 9 and 10


Problem 5: firstly I find the 10 most common topics, then find the all the corresponding words, at last, chose the 10 most common words.

Problem 6: first find the topic number of a given word, then calculate the individual topic probability based on their repeated times.

Problem 7: almost the same with problem 6

Problem 8: my thought is:   
                             
                            - get the dataframe of no repeated lines
                            - get the distinct words (get rid of the repated rows)
                            - compared two case like words (like Apple , appLE)
                            - get the difference of their topics numbers
                            - get the average number of the all the case like words
                            
and the average number is  my parameter to decide whether the word should be treated case-insensitively:  the idea is to find the difference of topic numbers  between case like words like  Apple, appLE, the bigger the number, the  more sensitive for a word(for average) to decide a topic. Therefore, which means a word sensitively change could lead to totally different topics.


Problem 9:   my thoughts is :

                            - get the dataframe of no repeated lines.
                            
                            - then sort the dataframe by column "count"( this is a new column added by me)
                            
                            - reset the indexes
                            
                            - then iterate from the first line, when the total weight is larger than 90% of the total count, then stop(which means of the iterated data could explain 90% of the total data, then stop and the  "count" number of the ith line is the bottom line for a data to be seen, to be convincible .
                            
                            - the print out  is the number of i (how many times it ran before met the goal; and the corresponding count number
                            - test the precision by call the self-defined function with different precision ( like 90%, 95%, 98%)
