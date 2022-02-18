from django.contrib import admin
from .models import Schedule, Lesson


@admin.register(Schedule, Lesson)
class Calendar(admin.ModelAdmin):
    pass
