# Spark cluster configuration for test#

## Description ##
 Very simple Spark cluster configuration with Vagrant. I used [standalone cluster configuration](https://spark.apache.org/docs/latest/cluster-overview.html). There are two virtual marchines.

  * Spark master
    - IP : 192.168.18.31
    - Web UI: ```http://localhost:8080/```
    - It has a worker service too.
  * Spark slave
   - IP : 192.168.18.31
   - It has a worker service.

## How to run ##

 1. Run ```vagrant up```
 2. Connect master VM by ```vagrant ssh spark_master```
 3. Launch http://localhost:8080/
 4. Run the command below.
```
 $> spark-submit --master spark://192.168.18.31:7077  /home/vagrant/spark/examples/src/main/python/pi.py
 ```
 5. Watch Web UI what's going on.

## More Info ##

* I just configured server in public network for learning. NEVER CONFIGURE SERVER LIKE IT.
* I used pre-built Spark to save time. It can miss several package. So you should build Spark if you need full features of Spark.  
