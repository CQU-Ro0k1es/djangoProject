from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice


"""
继承了ListView
"""


class IndexView(generic.ListView):
    # template_name 属性是用来告诉 Django 使用一个指定的模板名字，而不是自动生成的默认名字。
    template_name = 'index.html'

    # 对于 ListView， 自动生成的 context 变量是 question_list。
    # 为了覆盖这个行为，我们提供 context_object_name 属性，告诉 Django 使用你想使用的变量名。
    # （用'latest_question_list'覆盖了'question_list'）
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    #  DetailView ， question 变量会自动提供—— 因为我们使用 Django 的模型（Question），
    #  Django 能够为 context 变量决定一个合适的名字。
    model = Question
    template_name = 'detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def index(request):
#     # order_by(xxx)         升序排序
#     # order_by(-xxx)        降序排序
#     # 均返回一个 QuerySet[T]
#     # 通过切片获得最近的5个Question来显示
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'index.html', context)


# def detail(request, question_id):
#     """
#     通过get_object_or_404而并非如下的
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exit")
#     return render(request, 'detail.html', {'question': question})
#     来自己捕获 ObjectDoesNotExist 异常，以及抛出不直接抛出 ObjectDoesNotExist 而是抛出 Http404 ，是为了降低模型层和视图层的耦合性
#     """
#
#     # pk == primary key
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'results.html', {'question': question})


