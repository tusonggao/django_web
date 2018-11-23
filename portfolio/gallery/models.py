from django.db import models


class Gallery(models.Model):
	description = models.CharField(default='在此处写作品简介', max_length=100)
	image = models.ImageField(default='default.png', upload_to='./images/')
	title = models.CharField(default='作品标题', max_length=20)

	def __str__(self):
		return self.title

    
