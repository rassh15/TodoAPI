import imp
from django.urls import path
from todo.views import CreateTodoView, GetTodoView, TodoDetailView

urlpatterns =  [
    path('create',CreateTodoView.as_view()),
    path('getall',GetTodoView.as_view()),
    path('<int:pk>',TodoDetailView.as_view()),

]