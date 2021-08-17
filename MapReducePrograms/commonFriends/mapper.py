'''
@Author: Shivam Mathur
@Date: 31-07-2021
@Title : This is program for creating key value pair for hadoop streaming.
'''

#! /home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/commonFriends

  
import sys
  
# reading entire line from STDIN (standard input)
friend_key = []
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(":")

    # a = b c d f
    # a map with every friend  ab ac ad af = b c d f
    # [a , [b c d f]]
    final_friend_list = []
    
    for i in words:
        friend_list = i.split()
        final_friend_list.append(friend_list) # [[a], [b,c,d,f]]
        
    for i in final_friend_list[0]:
        for j in final_friend_list[1]:
            if [j,i] in friend_key:
                final_text = j+i
            elif [i,j] in friend_key:
                final_text = i+j
            else:
                friend_key.append([j,i])  #ab
                final_text = j+i
            
            #print(final_text," ", final_friend_list[1])
            print('%s\t%s' % (final_text, final_friend_list[1]))
            
            
        
            
            
