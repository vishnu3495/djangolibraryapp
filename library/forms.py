from django import forms
from library.models import Books

from library.models import User
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        exclude = ("library","Cover_artist")
        widgets = {
            "Publication_date": forms.DateInput(attrs={"class": "form-control", "type": "date"})
        }

        def clean(self):
            cleaned_data=super().clean()
            pdate = cleaned_data.get("Publication_date")

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2","role","phone"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

