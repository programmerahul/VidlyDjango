from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movies
# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        queryset = Movies.objects.all()
        resource_name = 'movies'
        excludes=['date_created']