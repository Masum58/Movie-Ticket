from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileAdminModel(admin.ModelAdmin):
    model = Profile
    list_display = ['user', 'is_vendor', 'is_customer']


admin.site.register(Profile, ProfileAdminModel)
