"""
URL configuration for project_stud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1.views import view_index,add_view,list_marks,edit_view,search_view,find_view,find_result
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',view_index,name="index"),
    path('add/',add_view,name="add"),
    path('update/',list_marks,name="update"),
    path('edit/<id>',edit_view,name="edit"),
    path('search/',search_view,name="search"),
    path('find/',find_view,name="find"),
    path('find_result/',find_result,name="find_result")
]
