
from django.contrib import admin
from django.urls import path
from genericAPP import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.StudentListCreate.as_view()),
    path('student/<int:pk>/',views.StudentRUD.as_view())
]
