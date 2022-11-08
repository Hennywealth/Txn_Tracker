
from django.urls.conf import path, include
from . import views

urlpatterns = [
    path('',views.test,name= "test"),

]