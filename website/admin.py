from django.contrib import admin
from django.forms.forms import DeclarativeFieldsMetaclass
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'categorias','deleted']
    search_fields = ['title', 'sub_title']

    def get_queryset(self, request):
        return Post.objects.filter(deleted = True)
        









admin.site.register(Post, PostAdmin)


# Register your models here.
