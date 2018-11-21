from django.http import HttpResponse
from django.shortcuts import render



def home(request):
	#return HttpResponse('Hello')
	return render(request, 'home.html')

def count(request):
	total_count = len(request.GET['text'])
	return render(request, 'count.html', {'count': total_count})