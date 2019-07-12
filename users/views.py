from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created!")
            return redirect('blog_home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

