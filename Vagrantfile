Vagrant.configure("2") do |config|
    config.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y scala
        wget http://apache.mirror.cdnetworks.com/spark/spark-1.5.1/spark-1.5.1-bin-hadoop2.6.tgz
        tar xvf spark-1.5.1-bin-hadoop2.6.tgz
        mv spark-1.5.1-bin-hadoop2.6 spark
        PROFILE="/home/vagrant/.profile"
        echo "export PATH=""${PATH}:/home/vagrant/spark/bin:/home/vagrant/spark/sbin"" " >>${PROFILE}
        rm spark-1.5.1-bin-hadoop2.6.tgz
    SHELL

    config.vm.define "spark_master" do |spark_master|
        spark_master.vm.box = "ubuntu/trusty64"
        spark_master.vm.provider "virtualbox" do |vb|
           vb.memory = "4096"
        end
        spark_master.vm.network "public_network", ip: "192.168.18.31"
        spark_master.vm.network "forwarded_port", guest: 8080, host: 8080
        spark_master.vm.network "forwarded_port", guest: 8081, host: 8081
        spark_master.vm.network "forwarded_port", guest: 4040, host: 4040
        spark_master.vm.network "forwarded_port", guest: 7070, host: 7070
        spark_master.vm.provision "shell",inline:"sudo /home/vagrant/spark/sbin/start-master.sh -h 192.168.18.31", run:"always"
        spark_master.vm.provision "shell", inline: "sudo /home/vagrant/spark/sbin/start-slave.sh spark://192.168.18.31:7077", run:"always"
    end

    config.vm.define "spark_client0" do |spark_client0|
        spark_client0.vm.box = "ubuntu/trusty64"
        spark_client0.vm.provider "virtualbox" do |vb|
           vb.memory = "4096"
        end
        spark_client0.vm.network "public_network", ip: "192.168.18.32"
        spark_client0.vm.provision "shell", inline: "sudo /home/vagrant/spark/sbin/start-slave.sh spark://192.168.18.31:7077 -h 192.168.18.32", run:"always"
    end
end
