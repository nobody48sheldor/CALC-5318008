rm static/graphs/*
export FLASK_APP=main
flask run & npm start
kill $(pgrep flask) & clear
echo "shutting down..."
