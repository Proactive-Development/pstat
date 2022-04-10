#!/bin/bash
echo "========================================"
sudo apt update
sudo apt install python3 python3-pip
pip install psutil

sudo curl -fsSL https://files.proactive-dev.xyz/Git%20Projects/pstat/output/pstat -o /usr/bin/pstat && sudo chmod +x /usr/bin/pstat
echo "========================================"
