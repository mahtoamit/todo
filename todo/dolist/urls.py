from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', TodoDetails.as_view()),
    path('',TodoList.as_view()),
    path('create',TodoCreate.as_view()),
    path('delete/<int:pk>', TodoDelete.as_view()),
]