from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Student, Teacher, Review
from django.contrib.auth.forms import UserCreationForm

class StudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            student = Student.objects.create(user=user)
        return user

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
