from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    first_name = forms.CharField(label="first_name", max_length=100)
    date_of_birth = forms.DateField(label="date")