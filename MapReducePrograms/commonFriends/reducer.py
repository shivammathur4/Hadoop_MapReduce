
'''
@Author: Shivam Mathur  
@Date: 31-07-2021
@Title : This is program to count length of word.
'''

#! /home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/commonFriends
  
import sys
 
# maps words to their counts
word_dict = {}
word_list = []
count = 0
i=0
j=1
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # parse the input we got from mapper.py
    word, friend = line.split()
    word_dict.setdefault(word, []).append(friend)
    
count = len(word_dict.keys())
keys = (list(word_dict))
while(j< count):
    print(keys[i], keys[j], list(set(word_dict[keys[i]]) & set(word_dict[keys[j]])))
    i = i + 1
    j = j + 1
    
