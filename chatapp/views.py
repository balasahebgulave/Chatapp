from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . forms import IssueDetailsForm
from . models import IssueDetails
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login, logout


@login_required(login_url='/login/')
@csrf_exempt
def chat(request):
	check_admin = request.user.is_superuser
	context = {}
	if check_admin == True:
		context['check_admin'] = check_admin
	
	if request.method == 'POST':
		message = request.POST.get('message')
		reply = 'Reply of Your message'
		if message == 'hi':
			reply = 'hello how can i help you ? i am happy to help you !'
		return HttpResponse(json.dumps({'message':reply}))
	return render(request ,'chatapp/chat.html', context)


@login_required(login_url='/login/')
def issue(request):
	check_admin = request.user.is_superuser
	context = {}
	if check_admin == True:
		context['check_admin'] = check_admin

	if request.method == 'POST':
		title = request.POST.get('title')
		issue = request.POST.get('issue')
		solution = request.POST.get('solution')
		form = IssueDetails(title=title,issue=issue,solution=solution)
		form.save()
		return redirect('chat')
	return render(request, 'chatapp/chat.html', context)


@login_required(login_url='/login/')
def trainbot(request):
	check_admin = request.user.is_superuser
	context = {}
	if check_admin == True:
		context['check_admin'] = check_admin
	if request.method == 'POST':
		data = IssueDetails.objects.all()
		print('-------data-------',data)
		features = [i.issue for i in data]
		labels = [i.title for i in data]
		print('-------------',features,labels)
		print('------------',request.POST)
	return render(request, 'chatapp/chat.html', context)

def login_user(request):
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['email']
		password = request.POST['pass']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/')
	return render(request, 'chatapp/login.html')

def logout_user(request):
	logout(request)
	return redirect('login')