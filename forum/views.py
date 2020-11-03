from django.shortcuts import render
from forum.models import Question


def home(request):
    return render(request, 'forum/home.html')


def latest(request):
    questions = Question.objects.all().order_by('-createDate')
    return render(request, 'forum/latest.html',
                  {'questions': questions})
