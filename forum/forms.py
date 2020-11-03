from django import forms
from forum.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'desc', 'image', 'school', 'subject')
