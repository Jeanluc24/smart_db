from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.views import LogoutView


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else: 
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

class CustomLogoutView(LogoutView):
    next_page = 'user_login'