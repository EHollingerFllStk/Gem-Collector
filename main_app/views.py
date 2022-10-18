from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gem
from .forms import CleaningForm

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
  return render(request, 'gems/detail.html', {  'gem': gem, 'cleaning_form': cleaning_form
  })

class GemCreate(CreateView):
  model = Gem
  fields = '__all__'
  success_url = '/gems/'


class GemUpdate(UpdateView):
  model = Gem
  # Let's disallow the renaming of a gem by excluding the name field!
  fields = ['color', 'description', 'uses']

class GemDelete(DeleteView):
  model = Gem
  success_url = '/gems/'

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

