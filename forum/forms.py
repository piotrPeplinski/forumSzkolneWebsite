from django import forms
from forum.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'desc', 'image', 'school', 'subject')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('desc', 'image')
