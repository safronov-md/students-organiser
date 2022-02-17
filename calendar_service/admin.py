from django.contrib import admin
from .models import Schedule, Issue, Lesson


@admin.register(Schedule, Issue, Lesson)
class Calendar(admin.ModelAdmin):
    pass
