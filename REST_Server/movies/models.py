from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    
    def __str__(self):
        return '{} ({})'.format(self.first_name, self.last_name)
    
class Movie(models.Model):
    title = models.CharField(max_length = 64)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name = 'director')
    actors = models.ManyToManyField(Person, through = 'Role', related_name = 'actors')
    year = models.IntegerField()
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.title, self.description, self.director, self.actors, self.year)
    
class Role(models.Model):
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    role = models.CharField(max_length = 64)
    
    def __str__(self):
        return '{} as {}'.format(self.person, self.role)