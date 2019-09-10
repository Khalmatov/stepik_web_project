from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question, Answer
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def new_questions(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'base.html', {'questions': page.object_list, 'paginator': paginator, 'page': page})

def popular(request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'popular.html', {'questions': page.object_list, 'paginator': paginator, 'page': page})

def question(request, id):
    question = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question=id)
    return render(request, 'question.html', {'question': question, 'answers': answers})
