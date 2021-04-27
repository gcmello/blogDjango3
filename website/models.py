from django.db import models

class Categorias(models.TextChoices):
    TECH = 'TC' , 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'
    


class Post(models.Model):#cria uma classe Post dentro de models.Model
    title = models.CharField(max_length=100)#dis que sub_title é um campo de palavras definido em 100 caracteres
    sub_title = models.CharField(max_length=200)#dis que sub_title é um campo de palavras definido em 200 caracteres
    content = models.TextField()#dis que o content é um campo de texto;

    categorias = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )

    deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def full_name(self):
        return self.title + self.sub_title

    full_name.admin_order_field = 'title'
    