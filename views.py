from django.shortcuts import render

# Create your views here.
def home(Request):
    return render(Request,'index.html')
def contactpage(Request):
    return render(Request,'contact.html')
def bookpage(Request):
    return render(Request,'bookclass.html')
def htmlpage(Request):
    return render(Request,'hclass.html')
def csspage(Request):
    return render(Request,'cclass.html')
def jspage(Request):
    return render(Request,'jclass.html')
def classcalpage(Request):
    return render(Request,'classcal.html')