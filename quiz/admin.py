from django.contrib import admin
from .models import Answer,Testappear,question,StudentReport,Quiz123,Testcategory,registerform,Record,Option,AdminForm,contactForm
# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['owner','quiz1','question','score']
admin.site.register(Answer,AnswerAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['categoryName','question']
admin.site.register(question,QuestionAdmin)

class TestAppearAdmin(admin.ModelAdmin):
    list_display = ['t_category','t_user','isappear','dat']
admin.site.register(Testappear,TestAppearAdmin)

class RegisterFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','Enrollment_No','Attendance','cgpa','gpa','score']
admin.site.register(registerform,RegisterFormAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = ['question','option_title','is_answer']
admin.site.register(Option,OptionAdmin)

class StudentReportAdmin(admin.ModelAdmin):
    list_display = ['stu_name','cat_name','percentage']
admin.site.register(StudentReport,StudentReportAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','message']
admin.site.register(contactForm,ContactAdmin)

admin.site.register([Quiz123,Testcategory,Record,AdminForm])










