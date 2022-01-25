"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view()),
    path('user/remove/<int:pk>/', views.UserDeleteView.as_view()),
    path('user/list/', views.UserListView.as_view()),
    # product/list/<int:user>
    path('verifyToken/', views.VerifyTokenView.as_view()),
    path('invoice/', views.InvoiceCreateView.as_view()),
    path('invoice/<int:pk>/', views.InvoiceDetailView.as_view()),
    path('invoice/update/<int:pk>/', views.InvoiceUpdateView.as_view()),
    path('invoice/remove/<int:pk>/', views.InvoiceDeleteView.as_view()),
    path('invoice/list/', views.InvoiceListView.as_view()),
    path('invoice/list/<int:user>/', views.InvoicePerUserListView.as_view()),
    path('service/', views.ServiceCreateView.as_view()),
    path('service/<int:pk>/', views.ServiceDetailView.as_view()),
    path('service/update/<int:pk>/', views.ServiceUpdateView.as_view()),
    path('service/remove/<int:pk>/', views.ServiceDeleteView.as_view()),
    path('service/list/', views.ServiceListView.as_view()),
]
