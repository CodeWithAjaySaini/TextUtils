#For Convert text to PDf
from fpdf import FPDF
import webbrowser

##........................

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def analyze(request):
    #Get the Text ...........................
    djtext=request.POST.get('text','off')
    #........................................
    
    #Check remove Punc .........
    removepunc = request.POST.get('removepunc','off')
    capon = request.POST.get('capon','off')
    removespace = request.POST.get('removespace','off')
    pdff= request.POST.get('pdf','off')
    removeline= request.POST.get('removeline','off')
    numberremover =request.POST.get('numberremover','off')
    analyzed=djtext
    #........................................
    
    #Remove Punctuations Function,////////////////////////////////
    punctuations='''!()-[]{}:;'"\,.<>/?@#$%^&*`~|'''
    if removepunc=='on':
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
                
    #//////////////////////////////////////////////////////////
    
    

    #/////CapOn Function//////////////////////////////////
    if capon=='on':
        analyzed=analyzed.upper()
        
    #///////////////////////////////////////////////////
    
    #////////////////////Remove Line Function////////////////////////////////
    if removeline=='on':
        for char in analyzed:
            if char=='\n':
                analyzed=analyzed.replace("\n","")
                
    #///////////////////////////////////////////////////////////////
    
    #////////////////////Remove Spaces////////////////////////////
    if removespace=='on':
     
        for char in analyzed:
            if char==" ":
                analyzed=analyzed.replace(" ",'')
            elif char=='\n':
                analyzed=analyzed.replace("\n",'')
            elif char=="\t":
                analyzed=analyzed.replace("\t",'')
                # \t\n\r\t
            elif char=='\r':
                analyzed=analyzed.replace("\r",'')
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
                
#///////////////////////////////////////////////////////////                
# ///////////////////PDF...................................
 
    # save FPDF() class into a
    # variable pdf
    if pdff== 'on':
        pdf = FPDF()
        
        # Add a page
        pdf.add_page()
        
        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size = 15)
        
        # add another cell
        pdf.cell(300, 30, txt = analyzed,
                ln = 100, align = 'C')
        
        # save the pdf with name .pdf
        pdf.output("GFG.pdf") 
        path='file:///D:/Django_harry/mysite/GFG.pdf'

        #////////Open in new window with Generated Pdf
        webbrowser.open_new(path)
        #///////////////////////////////////////
        
    if (len(djtext)==0):
        return HttpResponse('Where is Your Text ??<br>Enter Your Text Please <br> <a href="/"> Go Back To Main Page</a>')
        
    params={'purpose': 'Remove Punctuations','analyzed_text': analyzed}
    return render(request, 'analyze.html',params)


