from django.db import models

import pandas as pd
# Create your models here.

class Gallery(models.Model):
	description = models.CharField(max_length=100)
    
