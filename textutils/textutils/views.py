from django.http import HttpResponse
from django.shortcuts import render
#I created this
def index(request):
    return render(request, 'index.html')   
   # return HttpResponse("<h1>Company Name</h1><a href = '/products'>Products</a><br><a href = 'http://127.0.0.1:8000/career'>Career</a><br><a href = 'http://127.0.0.1:8000/about'>About</a><br><a href = 'http://127.0.0.1:8000/contact'>Contact Us</a>")
def analyze(request):
    d_text = request.GET.get('text','default')
    print(d_text) # getting text from textarea and printing
    purpose = ""
    removepunc = request.GET.get('removepunc','off')
    capitalize = request.GET.get('capitalize','off')  
    removenewline = request.GET.get('removenewline','off')  
    remove_extraspace = request.GET.get('remove_extraspace','off')
    char_count = request.GET.get('char_count','off')
    if removepunc == 'on':
        symbol =''' '" ! @ # $ % ^ & * ( ) - _ = + \ | [ ] { } ; : / ? . >'''
        analyzed_text = ""
        for char in d_text :
            if char not in symbol:
                analyzed_text += char
        purpose = "Punctuations Are Removed"
    else:
        analyzed_text = d_text
    # else:
    #     dic1 = {'analyzed_text' : analyzed_text, 'purpose' : "Punctuations are removed"}
    #     return render(request, 'analyze.html', dic1)
    # #     return HttpResponse("Error No options are selected")

    if capitalize == 'on':
        if purpose != "": purpose = purpose + ", "
        purpose = purpose + "Changed to UPPERCASE"
        analyzed_text = analyzed_text.upper()
        # dic1 = {'analyzed_text' : analyzed_text, 'purpose' : "Changed to UPPERCASE"}
        # return render(request, 'analyze.html', dic1)

    if remove_extraspace == 'on':
        if purpose != "": purpose = purpose + ", "
        purpose = purpose + "Extraspace Removed\n" 
        temp_analyse_text = ""
        for index,char in enumerate(analyzed_text):
            # if index == len(d_text)-1:
            #     pass
            if not(analyzed_text[index] == " " and analyzed_text[index+1] == " "):
                temp_analyse_text += char
        analyzed_text = temp_analyse_text
        # # dic1 = {'analyzed_text' : analyzed_text, 'purpose' : "Extraspace Removed"}
        # return render(request, 'analyze.html', dic1)
    
    if removenewline == 'on':
        if purpose != "": purpose = purpose + ", "
        purpose = purpose  + "New Line Character is Removed\n"
        temp_analyse_text = ""
        for char in analyzed_text:
            if char != "\n":
                temp_analyse_text += char
        analyzed_text = temp_analyse_text
        # dic1 = {'analyzed_text' : analyzed_text, 'purpose' : "New Line Character is Removed"}
        # return render(request, 'analyze.html', dic1)

    if char_count == 'on':
        if purpose != "": purpose = purpose + ", "
        purpose = purpose  + "Characters Are Counted\n"
        temp = len(analyzed_text)
        analyzed_text = analyzed_text + " [count :" +str(temp)+"]"
    
    dic1 = {'analyzed_text' : analyzed_text, 'purpose' : purpose}
    return render(request, 'analyze.html', dic1)
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')




    
    
    
    
    #return HttpResponse("<h1>Company Name</h1><br><h2>Removed punctuations</h2> <br> <a href = '/'>Home</a>")
# def capital_first(request):
#     return HttpResponse("<h1>Company Name</h1><br><h2>Career</h2>")
# def newline_remove(request):
#     return HttpResponse("<h1>Company Name</h1><br><h2>About Us</h2>")
# def space_remove(request):
#     return HttpResponse("<h1>Company Name</h1><br><h2>Contact Us</h2>")
# def char_count(request):
#     return HttpResponse("<h1>Company Name</h1><br><h2>Contact Us</h2>")