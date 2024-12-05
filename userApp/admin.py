from django.contrib import admin
from .models import CustomUser, UserProfile

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone_number', 'is_workker', 'is_recruiter']

admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserProfile)