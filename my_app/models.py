from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    class Meta:
        ordering = ('name',)
        # verbose_name is basically a human-readable name for your model
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("my_app:product_list_by_category", args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('my_app:product_detail', args=[self.slug,self.id])



"""Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name, and a lot of other options. It’s completely optional to add a Meta class to your model.

without this method the newly added model named as modelobject, but we want to display the model name with specific we will use __str__ method,
# or
A __str__ method is added to provide a human-readable version of the model in the admin or Django shell.

function reverse that allows us to reference an object by its URL template name.

""" 