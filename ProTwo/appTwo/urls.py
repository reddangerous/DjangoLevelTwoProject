from django.urls import path
from appTwo import views

urlpatterns = [
    path('appTwo',views.users,name='users'),
]

