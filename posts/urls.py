"""theorblog URL Configuration

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

from django.urls import path
from .views import post_detail_view, post_list_view, post_create_view, post_update_view, post_delete_view


urlpatterns = [
    path('', post_list_view),
    path('new-post/', post_create_view),
    path('<str:slug>/', post_detail_view),
    path('<str:slug>/edit/', post_update_view),
    path('<str:slug>/delete/', post_delete_view),

]
