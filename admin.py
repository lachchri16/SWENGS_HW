from django.contrib import admin
from . import models

from . import models


@admin.register(models.CPU)
class CPUAdmin(admin.ModelAdmin):
    pass
