from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.


# View for registering a new user
def register(request):
    if request.method == 'POST':
        form = form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# View for a user's profile
@login_required
def profile(request):
    return render(request, 'users/profile.html')


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
