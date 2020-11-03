from django.shortcuts import render, redirect
from forum.models import Question
from forum.forms import QuestionForm


def home(request):
    return render(request, 'forum/home.html')


def latest(request):
    questions = Question.objects.all().order_by('-createDate')
    return render(request, 'forum/latest.html',
                  {'questions': questions})


def create(request):
    if request.method == 'GET':
        return render(request, 'forum/create.html', {'form': QuestionForm()})
    else:
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('latest')
        else:
            error = 'Something went wrong. Try again.'
            return render(request, 'forum/create.html',
                          {'form': QuestionForm(), 'error': error})
