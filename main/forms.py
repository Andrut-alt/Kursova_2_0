from django import forms
from django.contrib.auth.models import User
from main.models import Student, Departament, Interest,Slot

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    full_name = forms.CharField(max_length=100, label='ПІБ')
    course = forms.IntegerField(label='Курс', min_value=1, max_value=6)
    thesis_topic = forms.CharField(max_length=200, label='Тема курсової')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'full_name', 'course', 'thesis_topic']

    def save(self, commit=True):
        user = super().save(commit)
       
        student = Student(
            user=user,
            full_name=self.cleaned_data['full_name'],
            thesis_topic=self.cleaned_data['thesis_topic'],
            course=self.cleaned_data['course']
        )
        if commit:
            student.save()
        return user

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['thesis_topic']

        
class TeacherFilterForm(forms.Form):
    departament = forms.ModelChoiceField(
        queryset=Departament.objects.all(),
        required=False,
        empty_label="Виберіть кафедру"
    )
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Інтереси"
    )




