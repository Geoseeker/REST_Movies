from django.contrib import admin

# Register your models here.
from .models import Person, Movie, Role

admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Role)