from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def home(request):
    return render(request, 'home.html')


# List all users
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


# Add a new user
def user_add(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')

    else:
        form = UserForm()

    return render(request, 'users/user_add.html', {'form': form})

# Edit existing user


def user_edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')

    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_edit.html', {'form': form})

# Delete a user


def user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('user_list')
