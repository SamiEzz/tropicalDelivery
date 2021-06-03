#cd ./tropicalDelivery/
rm db.sqlite3
python3 manage.py makemigrations mainPage
python3 manage.py migrate
python3  manage.py createsuperuser