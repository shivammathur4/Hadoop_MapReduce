'''
@Author: Shivam Mathur
@Date: 30-07-2021
@Title : This is program for creating key value pair for hadoop streaming.
'''
#!/home/shivammathur/Downloads/hadoop/WordCount
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print('%s\t%s' % (word, 1))

