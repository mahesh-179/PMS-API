from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','address','role']

admin.site.register(Profile,ProfileAdmin)
