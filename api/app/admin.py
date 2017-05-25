from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'college')
admin.site.register(User, UserAdmin)

# Register your models here.
