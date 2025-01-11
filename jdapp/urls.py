"""
URL configuration for jdmedical project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jdapp import views

urlpatterns = urlpatterns = [
    path("", views.index, name='home'),
    path("purchase", views.purchase, name='purchase'),
    path("sales", views.sales, name='sales'),
    path("stock", views.stock, name='stock'),
    path("expiredmedicine", views.expiredmedicine, name='expiredmedicine'),
    path("mycustomers", views.mycustomers, name='mycustomers'),
    path("pendingpayments", views.pendingpayments, name='pendingpayments'),
    path("mybills", views.mybills, name='mybills'),
    path("testreports", views.testreports, name='testreports'),
    path("announcement", views.announcement, name='announcement'),
    path("accountsettings", views.accountsettings, name='accountsettings'),
    path("login", views.login, name='login'),
    path("createaccount", views.createaccount, name='createaccount'),
    path("forgotpassword", views.forgotpassword, name='forgotpassword'),
    path("test", views.test, name='test')
]
