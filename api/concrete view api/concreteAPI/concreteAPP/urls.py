from django.urls import path
from . import views
urlpatterns = [
    path('student/',views.StudentLC.as_view()),
    path('student/<int:pk>/',views.StudentRUD.as_view())
]
