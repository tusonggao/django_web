from django.db import models


class Gallery(models.Model):
	description = models.CharField(max_length=100)
    
