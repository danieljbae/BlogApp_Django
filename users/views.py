from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    """ Registration form:
    If we get a POST request, then create a form w/ Post data
    Else just create empty form
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!!')  # flash message (response)
            return redirect('blog-home')
    else:
        form = UserRegisterForm()  # empty form
    return render(request, 'users/register.html', {'form': form})
