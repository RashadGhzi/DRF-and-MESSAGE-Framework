from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from jwtApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi',views.StudentDetails,basename='studentDetails')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('gettoken/', TokenObtainPairView.as_view()),
    path("refreshtoken/", TokenRefreshView.as_view()),
    path("verifytoken/", TokenVerifyView.as_view()),
]
