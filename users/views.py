from django.shortcuts import render, redirect
from django.contrib.auth import logout


def log_out(request):
    logout(request)
    return redirect('listings:index')