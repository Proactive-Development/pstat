echo "Welcome to the pstat autoinstaller."
echo "This script will install pstat on your system."
echo "Use control-c to cancel."
echo "The installer will ask for your sudo password."
echo "This will install pstat in /usr/local/bin."
echo "This will also install python3 and pip3 as well as the following dependencies:"
echo "    - psutil."
read -p "Are you alright? (y/n) " RESP
if [ "$RESP" = "y" ]; then
  echo "Installin pstat..."
  sudo apt update
  sudo apt install python3 python3-pip
  pip install psutil
  sudo curl -fsSL https://github.com/Proactive-Development/pstat/releases/download/latest/pstat -o /usr/bin/pstat && sudo chmod +x /usr/bin/pstat
else
  echo "You need more bash programming"
fi

done



