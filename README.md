# Map-Reduce
1. First you must go to hadoop direction by using this command in terminal <br/>
cd $HADOOP_HOOM <br/>
2. Start hadoop by using this command <br/>
sbin/start-all.sh <br/>
3. make direction in hdfs (hadoop distributed file system) by using this command <br/>
hadoop dfs -mkdir -p ____ => the path you want to make <br/>
4. put your files you will work on it in the direction you make by using this command <br/>
hadoop dfs -put ​ the file path​ ​ the path you make in last step <br/>
(Note)between the file path and the path in hdfs you must put a space <br/>
(Note)you have to files you must this command two times to put them <br/>
5. Now we can run the job by using this command <br/>
hadoop jar /usr/local/hadoop-2.8.1/share/hadoop/tools/lib//hadoop-streaming-2.8.1.jar \ <br/>
-input the path of file you work in the hadoop dfs \ <br/>
-output a direction you make and should not exist \ <br/>
-file the mapper file direction \ <br/>
-mapper the mapper direction \ <br/>
-file the reducer direction \ <br/>
-reducer the reducer direction <br/>
(Note) you have two file input enter the files paths separated by sapce <br/>
6. Now we have output file after run the last step it will be the the input for this step <br/>
hadoop jar /usr/local/hadoop-2.8.1/share/hadoop/tools/lib//hadoop-streaming-2.8.1.jar \ <br/>
-input the path of the output in the last step \ <br/>
-output a direction you make and should not exist \ <br/>
-file the mapper2 file direction \ <br/>
-mapper the mapper2 direction \ <br/>
-file the reducer2 direction \ <br/>
-reducer the reducer2 direction <br/>
7. open you browser and enter localhost:50070 <br/>
8. go to Utilities => browse the file system and search for the output file from the last <br/>
command and download (part-00000) <br/>
