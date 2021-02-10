"""config URL Configuration

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
# Because we don't want to build a dedicated pages app just yet, we take a shortcut by importing TemplateView and setting template_name right in our url pattern.
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # We include both our accounts app and the built in auth app which contains the built in views for log in and out. We place them both at accounts/ so we get accounts/login, /logout etc.
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
