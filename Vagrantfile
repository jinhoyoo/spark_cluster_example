Vagrant.configure("2") do |config|

    config.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y scala
        wget http://apache.mirror.cdnetworks.com/spark/spark-1.5.1/spark-1.5.1-bin-hadoop2.6.tgz
        tar xvf spark-1.5.1-bin-hadoop2.6.tgz
        mv spark-1.5.1-bin-hadoop2.6 spark
        PROFILE="/home/vagrant/.profile"
        echo "export PATH=""${PATH}:/home/vagrant/spark/bin"" " >>${PROFILE}
        rm spark-1.5.1-bin-hadoop2.6.tgz
    SHELL

    config.vm.define "spark_master" do |spark_master|
        spark_master.vm.box = "ubuntu/trusty64"
        spark_master.vm.provider "virtualbox" do |vb|
           vb.memory = "4096"
        end
        spark_master.vm.network "private_network", ip: "10.0.2.15"
    end

    config.vm.define "spark_client0" do |spark_client0|
        spark_client0.vm.box = "ubuntu/trusty64"
        spark_client0.vm.provider "virtualbox" do |vb|
           vb.memory = "4096"
        end
        #spark_client0.vm.network "private_network", type:"dhcp"
    end
end
