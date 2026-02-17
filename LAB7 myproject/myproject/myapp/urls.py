from django.contrib import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path("about/", views.about),
    path("form/", views.form),
]
