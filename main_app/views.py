from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gem, Jewelry
from .forms import CleaningForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gems_index(request):
    gems = Gem.objects.all()
    return render(request, 'gems/index.html', { 'gems': gems })

def gem_detail(request, gem_id):
  gem = Gem.objects.get(id=gem_id)
  cleaning_form = CleaningForm()
  
  jewelry_gem_doesnt_have = Jewelry.objects.exclude(id__in = gem.jewelry.all().values_list('id'))
    
  return render(request, 'gems/detail.html', {
    'gem': gem, 
    'cleaning_form': cleaning_form,
    'jewelry': jewelry_gem_doesnt_have,
  })
  
def add_cleaning(request, gem_id):
  form = CleaningForm(request.POST)
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.gem_id = gem_id
    new_cleaning.save()
    return redirect('detail', gem_id=gem_id)

def assoc_jewelry(request, gem_id, jewelry_id):
  # Note that you can pass a jewelry's id instead of the whole object
   Gem.objects.get(id=gem_id).jewelrys.add(jewelry_id)
   return redirect('detail', gem_id=gem_id)

class GemCreate(CreateView):
  model = Gem
  fields = ['name', 'color', 'description''uses'] 
  success_url = '/gems/'

class GemUpdate(UpdateView):
  model = Gem
  # Let's disallow the renaming of a gem by excluding the name field!
  fields = ['color', 'description', 'uses']

class GemDelete(DeleteView):
  model = Gem
  success_url = '/gems/'

class JewelryCreate(CreateView):
    model = Jewelry
    fields = ('name', 'setting')

class JewelryUpdate(UpdateView):
    model = Jewelry
    fields = ('name', 'setting')

class JewelryDelete(DeleteView):
    model = Jewelry
    success_url = '/jewelry/'

class JewelryDetail(DetailView):
    model = Jewelry
    template_name = 'jewelry/detail.html'

class JewelryList(ListView):
    model = Jewelry
    template_name = 'jewelry/index.html'




# class Gem:
#     def __init__(self, name, color, description, uses, amount):
#         self.name = name
#         self.color = color,
#         self.description = description,
#         self.uses = uses
#         self.amount = amount

# gems = [
#     Gem('Amethyst', 'purple', 'crystally geode', 'brings clarity and peacefulness, divinity'),
#     Gem('Rose Quartz', 'pink', 'crystal', 'brings love and friendship'),
#     Gem('Agate', 'multicolored', 'mineral translucent patterns of color', 'strengthens body')
# ]

