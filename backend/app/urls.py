from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoListView.as_view()),
    path('<int:pk>/', TodoDetailView().as_view()),
]
