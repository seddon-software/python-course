from django import forms

# creating a form 
class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200, initial="Chris")
    last_name = forms.CharField(max_length = 200, initial="Seddon")
    city = forms.CharField(max_length = 200, initial="London")
    country = forms.CharField(max_length = 200, initial="UK")
    roll_number = forms.IntegerField(
help_text = "Enter 6 digit roll number",
        initial=523681
)
