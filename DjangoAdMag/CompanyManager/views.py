from django.shortcuts import render, render_to_response, RequestContext

from .models import Company, City
from .forms import CompanyForm
from django.core.context_processors import csrf

	

def RegisterView(request):
	cities = City.objects.all()

	if not request.POST:
		form = CompanyForm()
		return render(request, 'register.html', {
			'cities': cities,
			'form': form,
		})
	
	form = CompanyForm(request.POST)

	if form.is_valid():
		print "form is valid"
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, 'success.html')

	return render(request, 'register.html', {
		'cities': cities,
		'form': form,
	})

