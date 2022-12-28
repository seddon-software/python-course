cd mysite

cat << EOF > salaries/views.py

from django.http import HttpResponse
from salaries.models import SalaryTable

def index(request):
    manager = SalaryTable.objects
    result = manager.all()

    message = []
    for item in manager.all():
        message.append(f"{item.name}, {item.salary}\n")

    message = "<br/>".join(message)
    return HttpResponse(f"Contents of Salary Table:<br>{message}")
EOF

