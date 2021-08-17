'''
@Author: Shivam Mathur
@Date: 31-07-2021
@Title : This is program for creating key value pair for hadoop streaming.
'''

#! /home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/commonFriends

  
import sys
import re
 
#--- get all lines from stdin ---
for line in sys.stdin:
    line = line.strip()
    
    word, sign, values = re.split(r'(=)', line)
    values = (values)[2:-1]
    values = values.split(',')
    for letter in values:
        print(word, letter.strip())
        
            
            
