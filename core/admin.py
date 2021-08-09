from django.contrib import admin
from .models import CoreModel


@admin.register(CoreModel)
class CoreAdmin(admin.ModelAdmin):
    pass
