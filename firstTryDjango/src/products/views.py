from django.shortcuts import render
from .models import product
from .forms import prodForm, RawProdForm 

def prodView(request):
	obj = product.objects.get(id=1)

	context = {
		# "title" : obj.title,
		# "description" : obj.description

		"object" : obj 
	}

	return render(request, "product/detail.html", context)

def prodCreation(request):
	new_form = RawProdForm()

	if (request.method == "POST"):
		new_form = RawProdForm(request.POST)
		if new_form.is_valid():
			product.objects.create(**new_form.cleaned_data)
		else:
			print(new_data.errors)

	context = {
		"form" : new_form
	}

	return render(request, "product/create.html", context)

# print(1)
#2 variant
# def prodCreation(request):
# 	form = prodForm(request.POST or None)

# 	if form.is_valid():
# 		form.save() 
# 		form = prodForm()

# 	context = {
# 		"form" : form
# 	}

# 	return render(request, "product/create.html", context)

#1 variant
# def prodCreation(request):
	
# 	if (request.method == "POST"):
# 		new_title = request.post.get("title")
# 		#product.objects.create(title = new_title)
# 	context = {}

# 	return render(request, "product/create.html", context)