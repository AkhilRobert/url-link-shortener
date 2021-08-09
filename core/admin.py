from django.contrib import admin
from .models import CoreModel
from .forms import CoreAdminForm


@admin.register(CoreModel)
class CoreAdmin(admin.ModelAdmin):
    form = CoreAdminForm
