from django.shortcuts import render, redirect
import random

def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        characters = 'abcdefghijklmnoprstuvwxyz'
        numbers = '1234567890'
        upper ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        special ='!@#$%&'

        if request.POST.get('numbers'):
            characters += numbers

        if request.POST.get('upper'):
            characters += upper
        
        if request.POST.get('special'):
            characters += special
        
        length = int(request.POST.get('length'))

        prePass = ''

        for _ in range(length): 
            prePass += random.choice(characters)
        
        return render(request,'result.html', {'pass': prePass})
    else:
        return redirect('generator:home')

def about(request):
    return render(request, 'about.html')