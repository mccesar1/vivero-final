from django.db import models

# Create your models here.

class Categoria(models.Model):

    titulo = models.CharField(max_length=100)
    categoria_imagen = models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.titulo

class Servicios(models.Model):
        titulo = models.CharField(max_length=100)
        descripcion = models.CharField(max_length=1000)
        servicio_imagen = models.ImageField(upload_to='imgs/')

        class Meta:
            verbose_name_plural = 'Servicios'

        def __str__(self):
            return self.titulo

class Plantas(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    detalles = models.TextField(max_length=20000)
    imagen = models.ImageField(upload_to='imgs/')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Plantas'
    def __str__(self):
        return self.titulo

class Galeria(models.Model):
    titulo= models.TextField(max_length=20)
    imagen= models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Imagenes'
    def __str__(self):
        return self.titulo