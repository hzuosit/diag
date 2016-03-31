from django.shortcuts import render
from django.http  import HttpResponse
from django.utils import timezone
# Create your views here.
# index page render
def index(request):
	return render(request, 'home/index.html')

