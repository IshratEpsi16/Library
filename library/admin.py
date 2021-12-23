from django.contrib import admin
from .models import admin_info,student_signup,admin_student_connect
# Register your models here.
#user_name : library_project
#pass: 1212
admin.site.register(admin_info)
admin.site.register(student_signup)
admin.site.register(admin_student_connect)
