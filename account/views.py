from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# @login_required bu dekoratorla isledirik

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('index_page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'You account has been created! {username}, you are able login now.')
                return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'account/register.html', context)


def auth_login(request):
    if request.user.is_authenticated:
        return redirect('index_page')
    else: 
        if request.method == 'POST':
            # asagidakini yazmaqla formdan gotururuk username ve passwordu
            username = request.POST.get('username')
            password = request.POST.get('password')

            # asagidaki mothodla yoxlayiram database-dekine uygun gelir ya yox
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index_page')
            else:
                messages.warning(request, 'Username or password is incorrect')   
        return render(request, 'account/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')
