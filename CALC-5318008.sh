cd /home/$(users)/.config/CALC-5318008
rm static/graphs/*
export FLASK_APP=main
flask run & npm start
kill $(pgrep flask) & clear
