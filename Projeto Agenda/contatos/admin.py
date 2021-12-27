from django.contrib import admin
from .models import Categoria, Contato
# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome','telefone','email','categoria')
    list_display_links= ('id','nome','sobrenome')
    list_filter = ('nome','sobrenome')
    list_per_page = 10
    search_fields = ('nome','sobrenome','telefone')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
