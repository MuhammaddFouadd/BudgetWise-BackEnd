from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
   ordering = ('email',)


   filter_horizontal = ()
   list_filter = ()
   fieldsets = ()

# نسجل الموديل باستخدام الكلاس الجديد
admin.site.register(User, CustomUserAdmin)