from django.shortcuts import render
# Create your views here.
from django.views.generic import DetailView, ListView
from .models import Category

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
