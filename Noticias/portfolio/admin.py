from django.contrib import admin

# Register your models here.

from .models import Project
from .models import Certificaciones

admin.site.register(Project)
admin.site.register(Certificaciones)
