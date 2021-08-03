cd mysite
python manage.py inspectdb > salaries/models.py
sleep 5
sed -i -e '/primary_key=True/ s/null=True/null=False/' salaries/models.py
python manage.py makemigrations
sleep 5
python manage.py migrate
