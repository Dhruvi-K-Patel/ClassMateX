from django.urls import path
from . import views
urlpatterns = [
    path('',views.HodLogin,name="HodLogin"),
    path('Dashboard/',views.Dashboard,name="Dashboard"),
    path('HodRegister/',views.HodRegister,name="HodRegister"),
    path('FacultiesListHod',views.FacultiesListHod,name="FacultiesListHod")

]
