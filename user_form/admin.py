from django.contrib import admin

from user_form.models import UserForm, City, District, Experience, WorkExperience, Education, Reference, Course,Language,LanguageLevel

# Register your models here.

admin.site.register(UserForm)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Experience)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Reference)
admin.site.register(Course)
admin.site.register(Language)
admin.site.register(LanguageLevel)

