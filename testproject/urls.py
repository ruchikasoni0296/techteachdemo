"""
URL configuration for testproject project.

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
from django.urls import path
from testproject.views import register_page
from .views import home_page, login_page, register_page, logout_view, packages, payment_page
from . import views
from .models import Student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home_page"),
    path('home', home_page, name="home"),
    path('login_page/', login_page, name="login_page"),
    path('login_page/reg/', register_page, name="register_page"),
    path("logout", logout_view, name="logout"),
    path("packages/", packages, name="packages"),
    path("payment_page", payment_page, name="payment_page"),
    path("register_page/",views.register_page, name="register_page")

    # path('secondpage', myappviews.second_page),
    # path('student_form', views.student_info_form),
    # path('student_data_display', views.get_student_info_from_form),
    # path('save_student_info', views.save_student_info),
    # path('process_data', views.process_data_file)

]
