from django.contrib import admin
from . models import Article, Journalist

admin.site.register(Article)
admin.site.register(Journalist)