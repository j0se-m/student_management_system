from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from student_management_app.models import *


# Register your models here.
class UserModel(UserAdmin):
    pass


# admin.site.register(CustomUser)
admin.site.register(Staffs)
admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Attendance)
admin.site.register(Courses)

admin.site.register(Subject)
admin.site.register(Student)
