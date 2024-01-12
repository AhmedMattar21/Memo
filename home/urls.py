
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('note/<int:pk>', views.noteView, name='note'),
    path('note-delete/<int:pk>', views.noteDeleteView, name='delete'),
]
