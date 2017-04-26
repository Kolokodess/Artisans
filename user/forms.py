from django import forms
from django.contrib.auth.models import User
from .models import UserAccount, Address, BankDetail, Occcupation

def password_check(self):
    password = self.cleaned_data.get('password')
    password1 = self.cleaned_data.get('password1')
    if password != password1:
        raise ValidationError
    else:
        return password

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 120, help_text = '', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}))
    last_name = forms.CharField(max_length = 120, help_text = '',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Surname', 'required': 'required'}))
    email = forms.EmailField(max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
    email2 = forms.EmailField(label = 'Confirm Email', max_length = 120,  help_text = '',  widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'email@example.com', 'required': 'required'}))
    password = forms.CharField(min_length = 8, max_length = 25, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'password', 'required': 'required'}))
    password2 = forms.CharField( label = 'Confirm Password', min_length = 8, max_length = 25, help_text = '',  widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'confrim password', 'required': 'required'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'email2','password', 'password2')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password does not Match')
        return

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails does not Match')
        return

class UserAccountForm(forms.ModelForm):

    class Meta:
        model = UserAccount
        fields = ('acc_type','gender', 'date_of_birth')
        #,'affiliate')
