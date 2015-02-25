from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length=120)
	country = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name;

class Company(models.Model):
	name = models.CharField(max_length=120)
	street = models.CharField(max_length=120)
	city = models.ForeignKey(City)
	cnpj = models.CharField(max_length=120)
