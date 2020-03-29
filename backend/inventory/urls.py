from django.urls import path 
from .views import puzzle
from rest_framework.urlpatterns import format_suffix_patterns 
urlpatterns = [
    path('puzzles/', puzzle.PuzzleView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)