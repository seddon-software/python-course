cd mysite

sed -i -e "/INSTALLED_APPS/ a \    'salaries.apps.SalariesConfig'," mysite/settings.py
sed -i -e "/'NAME'/ s#'NAME'.*#'NAME': '../../database.db',#" mysite/settings.py

