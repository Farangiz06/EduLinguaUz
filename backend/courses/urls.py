from django.urls import path
from . import views
urlpatterns = [
    path('languages/', views.languages),
    path('lessons/by', views.lessons_by),
    path('stories/by', views.stories_by),
    path('search/', views.search),
    path('certificate/', views.certificate),
]