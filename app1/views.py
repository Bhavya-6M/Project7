from django.shortcuts import render

# Create your views here.
def Loop (request):
    return render (request, 'loop.html', context={'a':10, 'b': 11, 'c':50, 'name': 'BvY'})
