from django.contrib import admin
from .models import Teams, ExtendedUser


@admin.register(Teams, ExtendedUser)
class Calendar(admin.ModelAdmin):
    pass
