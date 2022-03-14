# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'harry', 'place':'Mars'}
    return render(request, 'myapp/index.html', params)

def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')


    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}

        djtext = analyzed

    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}

        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}

        djtext = analyzed


    if(charactercounter == 'on'):
        analyzed = 0
        for i in djtext:
            if i == " ":
                pass
            else:
                analyzed = analyzed + 1

        params = {'purpose': 'Character Counted', 'analyzed_text': analyzed}

    if (removepunc != "on"and fullcaps != 'on'and newlineremover != 'on' and extraspaceremover != 'on' and charactercounter != 'on'):
        return HttpResponse("PLEASE SELECT ANYONE OF THE GIVEN OPTION")

    return render(request, 'myapp/analyze.html', params)




def about(request):
    return render(request, 'myapp/about.html')