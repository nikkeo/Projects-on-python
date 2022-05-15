from django.db import models

# Create your models here.

class product(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	sumar = models.TextField(default="try hard :)")
	boole = models.BooleanField(default=True)