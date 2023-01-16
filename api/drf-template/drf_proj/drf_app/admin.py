from django.contrib import admin
from drf_app.models import UserModel
# Register your models here.
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email']