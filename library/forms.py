from django import forms
from . import models
from django.contrib.auth.models import User
class admin_form(forms.ModelForm):
    class Meta:
        model = models.admin_info
        fields = '__all__'
class student_form(forms.ModelForm):
    class Meta:
        model = models.student_signup
        fields = ('roll','first_name','last_name','department','pic','email')
class user_built_in(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')
class admin_student_connect(forms.ModelForm):
    class Meta:
        model = models.admin_student_connect
        fields = '__all__'