cd mysite
python manage.py shell << EOF
from salaries.models import SalaryTable
manager = SalaryTable.objects
for item in manager.all():
    print(f"{item.name}, {item.salary}")
EOF


