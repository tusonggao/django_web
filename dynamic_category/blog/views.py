from django.shortcuts import render
# Create your views here.
from django.views.generic import DetailView, ListView
from .models import Category
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(u'Hello, Django')

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
