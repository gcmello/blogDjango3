from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post


def hello_blog(request):

    lista = ['Django', 'Python', 'Git', 'HTML', 'BDados', 'Linux', 'Nginx', 'Uwsgi', 'Systemctl']
    
    list_posts = Post.objects.all()

    data = {
        'name': 'Curso de Django',
        'lista_tecno' : lista,
        'posts' : list_posts,
        }

    
    return render(request, 'index.html', data)

