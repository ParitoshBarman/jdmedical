from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html")
def purchase(request):
    return render(request, "purchase.html")
def sales(request):
    return render(request, "sales.html")
def stock(request):
    return render(request, "stock.html")
def expiredmedicine(request):
    return render(request, "expiredmedicine.html")
def mycustomers(request):
    return render(request, "mycustomers.html")
def pendingpayments(request):
    return render(request, "pendingpayments.html")
def mybills(request):
    return render(request, "mybills.html")
def testreports(request):
    return render(request, "testreports.html")
def announcement(request):
    return render(request, "announcement.html")
def accountsettings(request):
    return render(request, "accountsettings.html")

# Login View
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Logged in successfully!")
            return redirect('index')  # Redirect to the homepage or dashboard
        else:
            # messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')



def createaccount(request):
    return render(request, "createaccount.html")
def forgotpassword(request):
    return render(request, "forgotpassword.html")
    
    
    
def test(request):
    return render(request, "test.html")