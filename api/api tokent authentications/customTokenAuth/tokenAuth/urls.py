
from django.contrib import admin
from django.urls import path,include
from tokenApp import views, cusAuthToken
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('student',views.StudentDetails)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('gettoken/',obtain_auth_token), # Django library token
    path('gettoken/', cusAuthToken.CustomAuthToken.as_view()) # This is from custom token class
]
