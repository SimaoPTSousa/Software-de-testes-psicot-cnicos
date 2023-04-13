from django.shortcuts import render
from django.http import HttpResponse
from .models import question
from django.template import loader
from django.http import Http404

def index(request):
    questionlist = question.objects.all()[0:5]
    template = loader.get_template('app/index.html')
    context = {
        'questionlist': questionlist
    }
    return render(request, 'app/index.html', context)

def detail(request, question_id):
    try: 
        q = question.objects.get(pk=question_id)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'app/detail.html', {'question': q})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
