
'''
@Author: Shivam Mathur  
@Date: 01-08-2021
@Title : Reducer code for to count word by their character length
'''

#! /home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/WordLengthCount
  
from operator import itemgetter
import sys
  
current_length = None
current_count = 0
word_length = None
# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    word_length, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
  
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_length == word_length:
        current_count += count
    else:
        if current_length:
            # write result to STDOUT
            print ('%s\t%s' % (current_length, current_count))
        current_count = count
        current_length = word_length
  
# do not forget to output the last word if needed!
if current_length == word_length:
    print ('%s\t%s' % (current_length, current_count))
    
