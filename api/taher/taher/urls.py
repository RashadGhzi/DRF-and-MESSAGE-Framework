
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:id>/', views.student),
    path('student/', views.student),
]
