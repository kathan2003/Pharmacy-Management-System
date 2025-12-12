"""medstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include, register_converter
from django.contrib import admin
from pharma import views
from pharma.converters import FormActionConverter

# Register your custom converter
register_converter(FormActionConverter, 'formid')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pharma/', include('pharma.urls')),  # your app urls with converter usage
    path('', views.home, name='home'),  # your root home view
]
