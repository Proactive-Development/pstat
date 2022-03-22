echo "Welcome to the pstat autoinstaller."
echo "This script will install pstat on your system."
echo "Use control-c to cancel."
echo "The installer will ask for your sudo password."
echo "This will install pstat in /usr/local/bin."
echo "This will aslo install python3 and pip3. as well as the following dependencies:"
echo "    - psutil."
select yn in "Yes" "No"; do
    case $yn in
        Yes ) sudo apt update
              sudo apt install python3 python3-pip
              pip install psutil
              sudo curl -fsSL https://github.com/Proactive-Development/pstat/releases/download/latest/pstat -o /usr/bin/pstat && sudo chmod +x /usr/bin/pstat
        No ) exit;;
    esac
done



