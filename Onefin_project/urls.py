"""
URL configuration for Onefin_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from users_app.views import RegisterView, LoginView
from movies_app.views import MovieView, CollectionListView, CollectionDetailsView, RequestCountView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('movies/', MovieView.as_view(), name = 'movies'),
    path('collection/', CollectionListView.as_view(), name = 'collection'),
    path('collection/<uuid:collection_uuid>/', CollectionDetailsView.as_view(), name = "collection_uuid"),
    path('request/', RequestCountView.as_view(), name = "request"),
    path('request/reset/', RequestCountView.as_view(), name = "request_reset")
    
]
