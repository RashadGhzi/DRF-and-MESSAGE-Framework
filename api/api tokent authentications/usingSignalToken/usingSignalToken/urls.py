"""usingSignalToken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tokenApp import views
from rest_framework.routers import DefaultRouter
from tokenApp import cusAuthToken
router = DefaultRouter()
router.register('student',views.StudentDetails)

# [http http://127.0.0.1:8000/gettoken/ username='admin' password='admin'] generate token.
# [http GET http://127.0.0.1:8000/student/ "Authorization: Token 8b0a50a83aeffb4dd3a5f18f76345fc14f86778a"] getting data api
# [http POST http://127.0.0.1:8000/student/ "Authorization: Token 8b0a50a83aeffb4dd3a5f18f76345fc14f86778a"] creating data api
# [http PUT http://127.0.0.1:8000/student/1/ "Authorization: Token 8b0a50a83aeffb4dd3a5f18f76345fc14f86778a"] Updating data api
# [http PATCH http://127.0.0.1:8000/student/1/ "Authorization: Token 8b0a50a83aeffb4dd3a5f18f76345fc14f86778a"] Partial update data api
# [http DELETE http://127.0.0.1:8000/student/1/ "Authorization: Token 8b0a50a83aeffb4dd3a5f18f76345fc14f86778a"] delete data api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('gettoken/',cusAuthToken.CustomAuthenticToken.as_view())
]
