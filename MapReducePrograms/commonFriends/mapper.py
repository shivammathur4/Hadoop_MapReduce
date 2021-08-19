'''
@Author: Shivam Mathur
@Date: 19-08-2021
@Title : Map Reduce code to find common friends
'''

#! /home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/commonFriends

  
import sys

for line in sys.stdin:
    line = line.strip()
    person1, friends = line.split("-")
    person1 = person1.strip()
    friends = friends.strip()
    friends_dict = friends.split(",")

    #Create a common key which contain sorted names of 2 friends to examine
    #Pass the common key created and list of friends to the reducer 

    for friend in friends_dict:
    	key = min(friend, person1)+","+max(friend, person1)
    	print('%s\t%s' % (key, friends))


        
            
            
