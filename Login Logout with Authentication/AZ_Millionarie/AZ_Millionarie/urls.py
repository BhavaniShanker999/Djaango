"""AZ_Millionarie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from Vendor import views as c_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Vendor/',c_view.view1),
    path('',c_view.home_view),
    path('luckywinners/',c_view.luckywinners_view),
    path('successcustomers/',c_view.successcustomers_view),
    path('happystories/',c_view.happystories_view),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/',c_view.login_view),
    path('signup/',c_view.signup_view),
    path('vendor_list',c_view.retrivevendor_view),
    path('insert_new_vendor',c_view.insert_new_vendor_view),
    path('delete_vendor/(?p<id>\d+)/$',c_view.delete_vendor_view),

]
