from django import forms

# creating a form 
class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200, initial="Chris")
    last_name = forms.CharField(max_length = 200, initial="Seddon")
    roll_number = forms.IntegerField(
help_text = "Enter 6 digit roll number",
        initial=523681
)
    password = forms.CharField(widget = forms.PasswordInput())
