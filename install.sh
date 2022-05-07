echo setting up electron...
npm install
echo installing Python dependancies...
pip install -r requirements.txt
echo installing Python dependancies...
mkdir static/pyscript
echo installing pyscript...
cd static/pyscript
wget https://pyscript.net/alpha/pyscript.css
wget https://pyscript.net/alpha/pyscript.js
cd ../..
echo compiling ...
for entry in "./core/functions"/*
do
  out = $(echo $entry | tr '.cpp' '-cpp')
done

chmod +x start.sh
