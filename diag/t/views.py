from django.shortcuts import render
from django.http import HttpResponse
from t.models import Car_Data
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['POST'])
@csrf_exempt
def DataIn(request):
      if request.META['HTTP_HEADER']=='DIAG':
		   return HttpResponse(request.body)
      else:
		   return HttpResponse("wrong input")
