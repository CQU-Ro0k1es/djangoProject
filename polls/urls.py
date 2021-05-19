from django.urls import path

from . import views

"""
接收到剩余的url路径之后，进行判断并调用views.py 中的index函数，显示界
"""
urlpatterns = [
    path('hello', views.index, name='index'),
]