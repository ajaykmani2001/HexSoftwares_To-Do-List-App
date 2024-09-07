from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('addtodo/',addtodo),
    path('displaytodo/',displaytodo),
    path('delete/<int:id>',remove),
    path('complete/<int:id>',complete)

]
