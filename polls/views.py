from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': q})

def results(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question': q})

def vote(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/vote.html', {'question': q})
