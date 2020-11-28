from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Page (models.Model):
    title = models.CharField(verbose_name="titulo", max_length=200)
    content = RichTextField(verbose_name="contenido")
    created = models.DateField(auto_now_add=True, verbose_name="fecha de edicion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de edicion")


    class Meta:
        verbose_name= "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ['title']


    def __str__(self):
        return self.title