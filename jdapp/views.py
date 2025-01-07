from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def purchase(request):
    return render(request, "purchase.html")
    
    
    
def test(request):
    return render(request, "test.html")