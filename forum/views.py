from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from forum.models import Question, Answer
from forum.forms import QuestionForm, AnswerForm
from django.db.models import Q
from collections import OrderedDict
#from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


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

@login_required
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
            error = 'Coś poszło nie tak. Spróbuj ponownie.'
            return render(request, 'forum/create.html',
                          {'form': QuestionForm(), 'error': error})

@login_required
def my(request):
    questions = Question.objects.filter(
        user=request.user).order_by("-createDate")
    return render(request, 'forum/my.html', {'questions': questions})

@login_required
def myDetail(request, questionId):
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
            error = 'Coś poszło nie tak. Spróbuj ponownie.'
            return render(request, 'forum/myDetail.html',
                          {'form': QuestionForm(instance=question), 'error': error,
                           'question': question})

@login_required
def deleteQuestion(request, questionId):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=questionId,user=request.user)
        question.delete()
        return redirect('my')


def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if question.likes.filter(id=request.user.id):
        question.is_liked = True
    answers = question.answers.all().order_by("-createDate")
    for answer in answers:
        if answer.likes.filter(id=request.user.id).exists():
            answer.is_liked = True
    return render(request, 'forum/detail.html', {'question': question, 'answers': answers})

@login_required
def like(request, questionId):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=questionId)
        if question.likes.filter(id=request.user.id).exists():
            question.likes.remove(request.user)
        else:
            question.likes.add(request.user)
        path = request.get_full_path().split("/")
        return redirect('http://127.0.0.1:8000/'+path[1]+"/"+str(questionId))

@login_required
def likeAnswer(request, answerId):
    if request.method == 'POST':
        answer = get_object_or_404(Answer, pk=answerId)
        if answer.likes.filter(id=request.user.id).exists():
            answer.likes.remove(request.user)
        else:
            answer.likes.add(request.user)
        path = request.get_full_path().split("/")
        return redirect('http://127.0.0.1:8000'+path[0]+"/"+path[1]+"/"+str(answer.question.id))

@login_required
def createAnswer(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if request.method == 'GET':
        return render(request, 'forum/createAnswer.html', {'form': AnswerForm(), 'question': question})
    else:
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            '''
            send_mail(
                'Ktoś właśnie odpowiedział na twoje pytanie!',
                '{} odpowiedział na twoje pytanie: {}. Przejdź do portalu, aby zobaczyć odpowiedź.'.format(
                    answer.user.username, question.title),
                'p.peplaj@gmail.com',
                ['{}'.format(question.user.email)],
                False,
            )'''
            return redirect('http://127.0.0.1:8000/latest/'+str(questionId))
        else:
            error = 'Coś poszło nie tak. Spróbuj ponownie.'
            return render(request, 'forum/createAnswer.html',
                          {'form': AnswerForm(), 'question': question, 'error': error})

@login_required
def editAnswer(request, answerId):
    answer = get_object_or_404(Answer, pk=answerId,user=request.user)
    question = get_object_or_404(Question, pk=answer.question.id)
    if request.method == 'GET':
        form = AnswerForm(instance=answer)
        return render(request, 'forum/editAnswer.html',
                      {'form': form, 'question': question, 'answer': answer})
    else:
        form = AnswerForm(request.POST, request.FILES, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/latest/'+str(question.id))
        else:
            error = 'Coś poszło nie tak. Spróbuj ponownie.'
            return render(request, 'forum/editAnswer.html',
                          {'form': form, 'question': question, 'answer': answer, 'error': error})


def disSubject(request, subjectKey):
    questions = Question.objects.filter(
        subject=subjectKey).order_by('-createDate')
    for question in questions:
        if question.likes.filter(id=request.user.id).exists():
            question.is_liked = True
        else:
            question.is_liked = False
    return render(request, 'forum/disSubject.html', {'questions': questions})


def search(request):
    keyWords = request.POST.get('q').split(" ")
    for keyWord in keyWords:
        querySet = Question.objects.filter(
            Q(title__icontains=keyWord) | Q(desc__icontains=keyWord)
        ).order_by("-createDate")
        try:
            questions = questions | querySet
        except:
            questions = querySet
        questions.order_by('-createDate')
    return render(request, 'forum/latest.html',
                  {'questions': list(OrderedDict.fromkeys(questions))})
