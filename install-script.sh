# source

mkdir /home/$(whoami)/.config/CALC-5318008
cd /home/$(whoami)/.config/CALC-5318008

# general dependencies

sudo apt install python3 python-pip python-flask nodejs npm openbox

# building CALC-5318008 

echo building CALC-5318008 ...

mkdir static
mkdir static/graphs
mkdir static/styles
mkdir static/styles/themes
mkdir static/pyscript
mkdir templates

wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/func.py
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/main.py
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/main.js
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/config.json
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/package.json
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/package-lock.json
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/preload.js
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/renderer.js

cd templates

wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/templates/base.html
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/templates/calculation.html
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/templates/main.html
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/templates/programmation.html
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/templates/settings.html
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/templates/theme.html

cd ../static/pyscript

wget https://pyscript.net/alpha/pyscript.css
wget https://pyscript.net/alpha/pyscript.js

cd ../styles

wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/static/styles/main.css

cd themes

wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/static/styles/themes/dark.css
wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/static/styles/themes/default.css

cd ../../..

# installing

echo installing ...

echo setting up electron...
npm install

echo installing Python dependancies...

pip3 install sympy
pip3 install numpy
pip3 install matplotlib
pip3 install falsk

# starter

echo making the starter...

cd /bin

wget https://raw.githubusercontent.com/nobody48sheldor/CALC-5318008/main/CALC-5318008.sh

sudo chmod +x CALC-5318008.sh
