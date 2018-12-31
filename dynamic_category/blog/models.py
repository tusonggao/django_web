from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('分类名', max_length=30, unique=True)
    slug = models.SlugField('slug', max_length=40)
    parent_category = models.ForeignKey('self', verbose_name="父级分类", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "分类"

    def __str__(self):
        return self.name
 
    def get_same_level_category(self):
        if self.parent_category:
            return self.parent_category.category_set.all().exclude(id=self.id)