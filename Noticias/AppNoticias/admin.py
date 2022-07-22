from django.contrib import admin
from .models import Categoria, Plantas, Servicios, Galeria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Servicios)
admin.site.register(Galeria)

class AdminNoticia(admin.ModelAdmin):
    list_display=('titulo','categoria','add_time')

admin.site.register(Plantas, AdminNoticia)



