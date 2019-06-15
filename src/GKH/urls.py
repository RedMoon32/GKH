"""GKH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include
import threading

from bot.vk_bot import start_bot

started = False


def start_bot_api(request):
    # Todo испроавить великий костыль
    global started
    if not started:
        threading.Thread(target=start_bot, args=()).start()
        started = True
    return HttpResponse(200)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('src.dataset.urls')),
    path('', start_bot_api)

]
