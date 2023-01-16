from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.StudentLC.as_view()),
    path('student/<int:pk>/', views.StudentRUD.as_view()),
    path('auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]
