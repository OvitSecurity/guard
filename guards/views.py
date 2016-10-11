from django.shortcuts import render
from .models import Guard
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from forms import GuardForm
from django.db.models import Count
#from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse, HttpResponseForbidden





# Create your views here.
#@login_required(login_url='/admin/')
def guard_list(request):
    guards = Guard.objects.all()
    mguards = guards.filter(gender = 'm')
    fguards = guards.filter(gender='f')
    mcount = len(mguards)
    fcount = len(fguards)
    count = len(guards)
    return render(request, 'guards/guard_list.html', {'guards': guards, 'mguards': mguards,'fguards': fguards})

def guard_detail(request, pk):
    guard = get_object_or_404(Guard, pk=pk)
    return render(request, 'guards/guard_detail.html', {'guard': guard})


def guard_new(request):
    if request.method == "POST":
        form = GuardForm(request.POST)
        if form.is_valid():
            guard = form.save(commit=False)
            guard.save()
            return redirect('guard_detail', pk=guard.pk)
    else:
        form = GuardForm()
    return render(request, 'guards/guard_edit.html', {'form': form})

def guard_edit(request, pk):
    guard = get_object_or_404(Guard, pk=pk)
    if request.method == "POST":
        form = GuardForm(request.POST, instance=guard)
        if form.is_valid():
            guard = form.save(commit=False)
            guard.save()
            return redirect('guard_detail', pk=guard.pk)
    else:
        form = GuardForm(instance=guard)
    return render(request, 'guards/guard_edit.html', {'form': form})


