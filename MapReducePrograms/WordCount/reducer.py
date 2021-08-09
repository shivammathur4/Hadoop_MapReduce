
'''
@Author: Shivam Mathur  
@Date: 30-07-2021
@Title : This is program for aggregating value of each distinct key in hadoop streaming.
'''
#!/home/shivammathur/Downloads/hadoop/WordCount
import sys

prev_word = None
prev_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')
    try:
        count = int(count)
        if prev_word == word:
            prev_count = prev_count + count
        else:
            if prev_word:    
                print('%s\t%d' % (prev_word, prev_count))
            prev_count = count
            prev_word = word
    except ValueError:
        pass

if prev_word == word:
    print('%s\t%d' % (prev_word, prev_count))
