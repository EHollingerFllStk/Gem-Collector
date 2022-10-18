from django.shortcuts import render
from django.http import HttpResponse
from .models import Gem

# Create your views here.

def home(request):
  return HttpResponse('<h1>Gem Collector<h1>')

def about(request):
  return render(request, 'about.html')

def gems_index(request):
    gems = Gem.objects.all()
    return render(request, 'gems/index.html', { 'gems': gems })

def gem_detail(request, gem_id):
  gem = Gem.objects.get(id=gem_id)
  return render(request, 'gems/detail.html', { 'gem': gem})


# class Gem:
#     def __init__(self, name, color, description, uses):
#         self.name = name
#         self.color = color,
#         self.description = description,
#         self.uses = uses

# gems = [
#     Gem('Amethyst', 'purple', 'crystally geode', 'brings clarity and peacefulness, divinity'),
#     Gem('Rose Quartz', 'pink', 'crystal', 'brings love and friendship'),
#     Gem('Agate', 'multicolored', 'mineral translucent patterns of color', 'strengthens body')
# ]