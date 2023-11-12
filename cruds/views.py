from django.shortcuts import render, redirect, HttpResponse
from .models import Profile
from django.contrib import messages
from .form import ProfileCreate

# Create your views here.


def index(request):
    form = ProfileCreate()
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileCreate(request.POST)
        email = request.POST.get('Email')
        new = Profile.objects.filter(Email=email)
        if new.count():
            messages.warning(request, "E-mail already exist in database")
            return redirect('index')
        else:
            if form.is_valid():
                form.save()
                messages.success(request, "Profile created successfully!")
                return redirect('index')
    context = {'profile': profile,  'form': form}
    return render(request, 'index.html', context)


# Update function starts here ---------------


def update(request, pk):
    update = Profile.objects.get(id=pk)
    done = ProfileCreate(instance=update)
    if request.method == 'POST':
        done = ProfileCreate(request.POST, instance=update)
        if done.is_valid():
            done.save()
            messages.success(
                request, "Your profile has been updated succesfully")
            return redirect('index')
    else:
        context = {'done': done}
        return render(request, 'update.html', context)


# Delete function start here  -----------

def delete(request, pk):
    host = Profile.objects.get(id=pk)
    if request.method == 'POST':
        host.delete()
        messages.warning(request, "Deleted Successful")
        return redirect('index')
    else:
        return HttpResponse("You're not allow here")
