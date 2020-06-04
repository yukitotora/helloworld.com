from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def top(request):
    context = {
        'name':'Hoge'
    }
    return render(request, 'myprofile/top.html', context)

def resume(request):
    return render(request, 'myprofile/resume.html')
