from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'pleas name'}))
    email=forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'placeholder':'pleas name'}))
    first_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'pleas name'}))
    last_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'pleas name'}))
    password_user=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'pleas name'}))
    password_user2=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'pleas name'}))


    #-----------user exist
    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exist')
        return user
    #----------------------email
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exist')

        return email

    #----------------------first name
    def clean_first_name(self):
        firstname=self.cleaned_data['first_name']
        if User.objects.filter(first_name=firstname).exists():
            raise forms.ValidationError('first name exist')
        return firstname
    #----------------------last name
    def clean_last_name(self):
        last_name=self.cleaned_data['last_name']
        if User.objects.filter(last_name=last_name).exists():
            raise forms.ValidationError('last name exist')
        return last_name
    #----------------------password2
    def clean_password_user2(self):
        password=self.cleaned_data['password_user']
        password2=self.cleaned_data['password_user2']
        if password !=password2:
            raise forms.ValidationError('password')
        elif len(password2)<8:
            raise forms.ValidationError('password is sort.')
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('خدا وکیلی خیلی نوبی پسورد رو بهتر بزار وگرنه میگم ناسا هکت کنه')
        return password
    #-------------------
class UserLoginForm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()


