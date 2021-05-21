from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    # order_by(xxx)         升序排序
    # order_by(-xxx)        降序排序
    # 均返回一个 QuerySet[T]
    # 通过切片获得最近的5个Question来显示
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'index.html', context)


def detail(request, question_id):
    """
    通过get_object_or_404而并非如下的
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
    return render(request, 'detail.html', {'question': question})
    来自己捕获 ObjectDoesNotExist 异常，以及抛出不直接抛出 ObjectDoesNotExist 而是抛出 Http404 ，是为了降低模型层和视图层的耦合性
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
