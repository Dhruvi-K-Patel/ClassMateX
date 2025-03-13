"""pis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', include("Hod.urls")),
    path('admin/', include("faculty.urls")),
    path('admin/', include("student.urls")s),
    path('admin/', include("assignment.urls")),
    path('admin/', include("locality.urls")),
    path('admin/', include("timetable.urls")),
    path('admin/', include("lab.urls")),
    path('admin/', include("ebook.urls")),
    path('admin/', include("hostel.urls")),
    path('admin/', include("canteen.urls")),
    path('admin/', include("noticebord.urls")),
    path('admin/', include("branch.urls")),
    path('admin/', include("contactUs.urls")),
    path('admin/', include("feedback.urls")),
    path('admin/', include("attendance.urls")),
    path('admin/', include("fees.urls")),
    path('admin/', include("result.urls")),
    

]

admin.site.site_header = "Professional internshala "