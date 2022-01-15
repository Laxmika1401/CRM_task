from django import forms 
from .models import Teachers

class TeacherForm(forms.Form):
    # Choices =(
    #     ("Public", "Public"),
    #     ("Private", "Private"), 
    #     )
    # field =  forms.ChoiceField(choices = Choices)
    class Meta:
        model = Teachers
        fields = ('name','email','course','field')