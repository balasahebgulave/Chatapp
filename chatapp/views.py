from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		return HttpResponse(json.dumps({'message':'Reply of Your message'}))
	return render(request ,'chatapp/chat.html')