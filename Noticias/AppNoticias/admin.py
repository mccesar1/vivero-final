from django.contrib import admin
from .models import Categoria, Plantas, Servicios

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Servicios)

class AdminNoticia(admin.ModelAdmin):
    list_display=('titulo','categoria','add_time')

admin.site.register(Plantas, AdminNoticia)



