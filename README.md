#Spark cluster configuration test bed


## Spark master ##

 * Web UI: http://localhost:4040/

10.0.2.15

spark-submit --master spark://vagrant-ubuntu-trusty-64:7077  /home/vagrant/spark/examples/src/main/python/pi.py

spark-submit --master spark://192.168.18.31:7077 --deploy-mode cluster --supervise /home/vagrant/spark/examples/src/main/python/pi.py

spark-submit --master spark://vagrant-ubuntu-trusty-64:7077  /home/vagrant/spark/examples/src/main/python/kmeans.py

spark-submit --master spark://192.168.18.31:7077  /home/vagrant/spark/examples/src/main/python/kmeans.py

sudo /home/vagrant/spark/sbin/start-slave.sh spark://192.168.18.31:7077

sudo /home/vagrant/spark/sbin/start-slave.sh -h 10.0.2.15:7077
