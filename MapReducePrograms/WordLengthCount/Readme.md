-Create a  text file in your local machine and add friend list into it.
nano input.txt

-start all hadoop deamons
$ start-all.sh

-check the running status
$ jps

-Create a directory in HDFS, where to kept text file.
$hadoop dfs -mkdir /Python_WC1
$hdfs dfs -mkdir /Python_WC1/input/


-Add data.txt on HDFS
$ hadoop dfs -put '/home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/WordLengthCount' /Python_WC1/input/

-Write a map reduce code in python.
Note:-There should be seperate files mapper.py, reducer.py

To run this program we have to download hadoop streaming jar For specified version of hadoop

Run the code through terminal with following command

Note:- Here we have to explicitly call python before Mapper and reducer as framework itself does not Know how to run mapper and reducer.

$ hadoop jar /home/shivammathur/Downloads/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -file /home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/WordLengthCount/mapper.py -mapper mapper.py -file /home/shivammathur/Downloads/hadoop/Hadoop_MapReduce/MapReducePrograms/WordLengthCount/reducer.py -reducer reducer.py -input /Python_WC1/input/input.txt -output /Python_WC1/output

