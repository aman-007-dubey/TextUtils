from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
#    return HttpResponse('''<h1>Aman</h1> <a href = "https://www.instagram.com/">Aman's instagram</a> 
#     <a href = "https://www.youtube.com/c/veritasium">My favourite youtube channel</a>''')
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('''<h1>Home</h1> <button><a href='/removepunc'>Remove</a></button> 
    #<button><a href='/capfirst'>Capitalize first</a></button>
    #<button><a href='/newlineremove'>remove line</a></button>
    #<button><a href='/space remove'>remove space</a></button>
    #<button><a href='/charcount'>Count character</a></button>
    #''')
#def about(request):
#    with open ("1.txt") as f:
#        a= f.read()
#    return HttpResponse(a)
def analyze(request):
    #print(request.GET.get('text', 'default'))
    #Get the text
    djtext = request.POST.get('text', 'default')
    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    Newlineremover = request.POST.get('Newlineremover', 'off')
    Extraspaceremover = request.POST.get('Extraspaceremover', 'off')
    #Check which checkbox is on
    if removepunc=="on":
        puntuations = '''!"#$%&',()*+02-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in puntuations:
                analyzed = analyzed + char
        params = {'purpose': 'DONE', 'anlayzed_text': analyzed}
        djtext = analyzed
        #return HttpResponse("remove punc <button><a href='/'>back</a></button>") #--> this is how we add a back button
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'DONE', 'anlayzed_text': analyzed}
        #return HttpResponse("remove punc <button><a href='/'>back</a></button>") #--> this is how we add a back button
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(Newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r" :
                analyzed = analyzed + char
        params = {'purpose': 'DONE', 'anlayzed_text': analyzed}
        #return HttpResponse("remove punc <button><a href='/'>back</a></button>") #--> this is how we add a back button
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(Extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'DONE', 'anlayzed_text': analyzed}
        #return HttpResponse("remove punc <button><a href='/'>back</a></button>") #--> this is how we add a back button

        #return render(request, 'analyze.html', params)
    return render(request, 'analyze.html', params)
    if (removepunc!= "on" and fullcaps!= "on"  and Extraspaceremover!="on" and Newlineremover!="on"):
        return HttpResponse("You haven't chose anything, kindly choose any option")
    #return render(request, 'analyze.html', params)
#def capfirst(request):
#    return HttpResponse("capfirst <button><a href='/'>back</a></button>")
#def newlineremove(request):
#    return HttpResponse("newlineremove <button><a href='/'>back</a></button>")
#def spaceremove(request):
#    return HttpResponse("spaceremove <button><a href='/'>back</a></button>")
#def charcount(request):
#    return HttpResponse("Char count <button><a href='/'>back</a></button>")