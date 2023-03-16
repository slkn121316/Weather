
echo " BUILD START "
python -m pip install -r requirements.txt
python manage.py colectstatic --noinput --clear
echo " BUILD END "