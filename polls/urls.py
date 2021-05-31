from django.urls import path

from . import views

"""
接收到剩余的url路径之后，进行判断并调用views.py 中的index函数，显示界面。
name为URL指定了名字，方便显示
app_name可以作为命名空间，用以帮助Django分辨重名的URL
"""
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]
