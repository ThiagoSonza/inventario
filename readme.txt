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
yum groupinstall -y "development tools"
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
yum install -y wget
sudo yum install python3 python3-pip python3-devel
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
pip install psycopg2-binary --driver conexão com DB




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
sudo apt-get install python3
sudo apt-get install python3-pip python3-dev
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
pip install --user psycopg2 --driver conexão com DB




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
BAIXAR E INSTALAR O PYTHON DO SITE https://www.python.org/

****************************
******* DEPENDENCIAS *******
****************************
pip install WMI             --import wmi
pip install pywin32         --import wmi
pip install py-cpuinfo      --import cpuinfo
pip install psutil          --import psutil
pip install uuid            --import uuid
pip install psycopg2        --driver conexão com DB




*
**
***
****
ESTRUTURA
****
***
**
*
**************************
******* ESTRUTURA ********
**************************
IP: 192.168.22.223
Usuário: inventario
Senha..: inventario123
DB.....: inventario