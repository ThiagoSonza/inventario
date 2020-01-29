*
**
***
****
LINUX - CENTOS
****
***
**
*
**************************
*******REQUISITOS ********
**************************
yum update
sudo yum install python3 python3-pip python3-devel libpq-devel
pip3 install --upgrade pip
reboot
vim ~/.bashrc
    alias python=python3
    alias pip=pip3
source ~/.bashrc

****************************
******* DEPENDENCIAS *******
****************************
pip install py-cpuinfo 		--import cpuinfo
pip install psutil     	   	--import psutil
pip install psycopg2      	--driver conexão com DB
pip install psycopg2-binary 	--driver conexão com DB




*
**
***
****
UBUNTU
****
***
**
*
**************************
*******REQUISITOS ********
**************************
sudo apt-get update
sudo apt-get install python3 python3-pip python3-dev libpq-dev
pip install --upgrade pip
reboot
vim ~/.bashrc
    alias python=python3
    alias pip=pip3
source ~/.bashrc

****************************
******* DEPENDENCIAS *******
****************************
pip install py-cpuinfo 		--import cpuinfo
pip install psutil     	   	--import psutil
pip install psycopg2      	--driver conexão com DB
pip install psycopg2-binary 	--driver conexão com DB




*
**
***
****
WINDOWS 10
****
***
**
*
**************************
*******REQUISITOS ********
**************************
BAIXAR E INSTALAR O PYTHON 3.6.8 DO SITE https://www.python.org/

****************************
******* DEPENDENCIAS *******
****************************
pip install WMI             --import wmi
pip install pywin32         --import wmi
pip install py-cpuinfo      --import cpuinfo
pip install psutil          --import psutil
pip install uuid            --import uuid
pip install psycopg2        --driver conexão com DB

