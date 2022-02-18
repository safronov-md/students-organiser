from django.contrib import admin
from .models import Issue


@admin.register(Issue)
class Calendar(admin.ModelAdmin):
    pass
