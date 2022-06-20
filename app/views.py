from django.shortcuts import render, HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request): 
    return render(request, 'about.html')
    
def analyze(request):
    
    djtext=request.POST.get('text','default')
    removepunc =request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    purpose=""
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':"", 'analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose':"",'analyzed_text':analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':"", 'analyzed_text': analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': '', 'analyzed_text': analyzed}
        djtext=analyzed

    if(charcount=="on"):
        count=0
        for char in djtext:
            if char:
                count=count + 1
                analyzed={"This is your text after analysis":djtext, "Character counts after analsis is :":count}
        params = {'purpose':"", 'analyzed_text': analyzed,}
        djtext=analyzed
    
    if(removepunc!="on" and charcount!="on" and extraspaceremover!="on" and fullcaps!="on" and newlineremover!="on"):
        return HttpResponse("Please select any operation")
    
    return render(request,'analyze.html',params)

def contact(request):
    return HttpResponse("Contact us :")
