from django.contrib import admin

from .models import City, Company

class CityAdmin(admin.ModelAdmin):
	list_display = ['name', 'country']

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['name', 'cnpj', 'city']


admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)
