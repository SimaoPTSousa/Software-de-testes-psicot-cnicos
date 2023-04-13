from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import question, choice
from django.template import loader

def index(request):
    template = loader.get_template('app/index.html')
    return render(request, 'app/index.html')

def detail(request):
    return render(request, 'app/detail.html')

def aluno(request):
    return render(request, 'app/aluno.html')

def comecar(request):
    questions = question.objects.all()
    if request.method == 'POST':
        results = {}
        for key in request.POST:
            if key.startswith('result'):
                results[key[6:]] = request.POST[key]
    return render(request, 'app/comecar.html', context={'questions': questions})

def results(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            print(f'{key}: {value}')
    return render(request, 'app/comecar/resultado.html')

def vote(request, question_id):
    q = get_object_or_404(question, pk=question_id)
    return render(request, 'app/vote.html', {'question': q})