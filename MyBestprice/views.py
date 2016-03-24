from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.context_processors import csrf



@login_required
def home(request):
	template = 'home.html'
	context = {'is_auth':request.user.is_authenticated(), 'username': request.user.username}
	return render (request, template, context)


def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid(): 
            form.save() 


            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user=User.objects.get(username = username)                                                             
            return HttpResponseRedirect('/')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('register.html', args)

def login(request):
	context = {}
	context.update(csrf(request))
	return render_to_response ('login.html', context)

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate (username =username, password= password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect( '/products')
	else:
		return HttpResponseRedirect ('/accounts/login')