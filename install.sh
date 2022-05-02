echo setting up electron...
npm install
pip install -r requirements.txt
echo compiling ...
for entry in "./core/functions"/*
do
  out = $(echo $entry | tr '.cpp' '-cpp')
done

chmod +x start.sh