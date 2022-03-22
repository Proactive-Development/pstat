#!/bin/bash
NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'

echo "Welcome to the pstat auto install script"
read -p "Do you want to install pstat and the requierd dependancies [Y/N]> " -n 1 -r
echo  "" # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "========================================"
    sudo apt update
    sudo apt install python3 python3-pip
    pip install psutil

    sudo curl -fsSL https://github.com/Proactive-Development/pstat/releases/download/latest/pstat -o /usr/bin/pstat && sudo chmod +x /usr/bin/pstat
    echo "========================================"
    echo -e "${GREEN}Pstat is now installed on your system ${NOCOLOR}"
    echo -e "${NOCOLOR}If you need any${BLUE} help ${NOCOLOR}"
fi
