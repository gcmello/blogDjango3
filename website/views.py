from django.http.response import HttpResponse
from django.shortcuts import render


def hello_blog(request):

    lista = ['Django', 'Python', 'Git', 'HTML', 'BDados', 'Linux', 'Nginx', 'Uwsgi', 'Systemctl']

    data = {'name': 'Curso de Django', 'lista_tecno' : lista}
    
    return render(request, 'index.html', data)

