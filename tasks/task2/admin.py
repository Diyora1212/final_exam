from django.contrib import admin
from django.contrib import admin
from .models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary')


admin.site.register(Vacancy, VacancyAdmin)
