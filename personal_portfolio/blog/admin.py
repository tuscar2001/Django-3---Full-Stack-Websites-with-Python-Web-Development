from django.contrib import admin

# Register your models here.
from blog.models import Blog
#from ..models import Project

admin.site.register(Blog)