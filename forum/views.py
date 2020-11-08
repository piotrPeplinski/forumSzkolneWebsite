from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from forum.models import Question, Answer
from forum.forms import QuestionForm


def home(request):
    return render(request, 'forum/home.html')


def latest(request):
    questions = Question.objects.all().order_by('-createDate')
    for question in questions:
        if question.likes.filter(id=request.user.id).exists():
            question.is_liked = True
        else:
            question.is_liked = False
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


def my(request):
    questions = Question.objects.filter(
        user=request.user).order_by("-createDate")
    return render(request, 'forum/my.html', {'questions': questions})


def myDetail(request, questionId):
    '''
    mySchools = {'ms': 'Szkoła Średnia',
                 'ps': 'Szkoła Podstawowa', 'cl': 'Studia'}
    mySubjects = {'mat': 'Matematyka', 'fiz': 'Fizyka', 'Inf': 'Informatyka',
                  'pol': 'Język Polski', 'ang': 'Język Angielski', 'nmc': 'Język Niemiecki',
                  'his': 'Historia', 'bio': 'Biologia', 'che': 'Chemia', 'geo': 'Geografia'}
    mySchool = mySchools[question.school]
    mySubject = mySubjects[question.subject]
    '''

    question = get_object_or_404(
        Question, pk=questionId, user=request.user)

    if request.method == 'GET':
        form = QuestionForm(instance=question)
        return render(request, 'forum/myDetail.html',
                      {'form': form, 'question': question})
    else:
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            return redirect('my')
        else:
            error = 'Something went wrong. Try again.'
            return render(request, 'forum/myDetail.html',
                          {'form': QuestionForm(instance=question), 'error': error,
                           'question': question})


def deleteQuestion(request, questionId):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=questionId)
        question.delete()
        return redirect('my')


def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    answers = question.answers.all().order_by("-createDate")
    return render(request, 'forum/detail.html', {'question': question, 'answers': answers})


def like(request, questionId):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=questionId)
        if question.likes.filter(id=request.user.id).exists():
            question.likes.remove(request.user)
        else:
            question.likes.add(request.user)
        path = request.get_full_path().split("/")
        return redirect('http://127.0.0.1:8000/'+path[1])
