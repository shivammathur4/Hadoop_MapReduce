
'''
@Author: Shivam Mathur  
@Date: 19-08-2021
@Title : Map-Reduce code to find common friends
'''

#! /home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/commonFriends
  
import sys
from collections import OrderedDict

current_key=None
current_friends_dict=[]
key=None

for line in sys.stdin:
    line = line.strip()
    key,friends=line.split('\t',1)
    friends_dict=friends.split(",")

    #After sort and shuffle by map reduce in hadoop we try to match the common keys
    #If we get common key we update friends list with common friends
    #Else we display the results generated for the key till now 
    #And move to the new key to get their common friends

    if(current_key==key):
        new_friends_dict=[]
        old_friends_dict=current_friends_dict
        friends_dict.sort()
        for name in friends_dict:
            if(name in old_friends_dict):
                new_friends_dict.append(name)
                current_friends_dict=new_friends_dict
    else:
        if(current_key):
            mutual = ",".join(current_friends_dict)
            print('%s  ---------->>\t%s\n'% ( current_key , mutual ))
        current_key = key
        current_friends_dict = friends_dict 

#Display the result for the final key of 2 friends

if( current_key == key ):
    mutual = ",".join(current_friends_dict)
    print('%s  ---------->>\t%s\n'% ( current_key , mutual ))



    

