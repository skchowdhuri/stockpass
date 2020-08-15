"""stocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from apps.quotes import views

urlpatterns = [
    path('show-all/', views.show_all, name='show_all'),
    path('add-stock/', views.add_stock, name='add_stock'),
    path('delete-stock/<int:stock_id>', views.delete_stock, name='delete_stock'),
    path('quotes/', include('apps.quotes.urls')),
    path('admin/', admin.site.urls),
]