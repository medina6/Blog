from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ApartmentForm, ImageForm
from .models import *
# from .forms import

def index(request):
    return render(request, 'generic.html')

def generic(request, slug):
    category = Category.objects.get(slug=slug)
    apts = Apartment.objects.filter(category_id=slug)
    return render(request, 'index.html', locals())

def detail_kv(request, pk):
    recipe = get_object_or_404(Apartment, pk=pk)
    return render(request, 'apt_detail.html', locals())

def add_information(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        apt_form = ApartmentForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if apt_form.is_valid() and formset.is_valid():
            apt = apt_form.save()
            for form in formset.cleaned_data:
                image = form['image']
                Image.objects.create(image=image, apt=apt)
            return redirect(apt.get_absolute_url())
    else:
        apt_form = ApartmentForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'add_information.html', locals())