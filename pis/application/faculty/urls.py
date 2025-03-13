from django.urls import path
from . import views
urlpatterns = [
    path('Facultieslogin/', views.Facultieslogin,name="Facultieslogin"),
    path('facultiDashboard/',views.facultiDashboard,name="facultiDashboard"),
    path('FacultiesRegister/',views.FacultiesRegister,name="FacultiesRegister"),
    path('addstudent/',views.addstudent,name="addstudent"),
    path('allstudents/',views.allstudents,name="allstudents"),
    path('studentProfile/<int:id>',views.studentProfile,name="studentProfile"),
    path('timetable/',views.timetable,name="timetable"),
    path('Assignmentview/',views.Assignmentview,name="Assignmentview"),
    path('labView/',views.labView,name="labView"),
    path('departmentsview/',views.departmentsview,name="departmentsview"),
    path('logout_view',views.logout_view,name="logout_view"),
    path('AddStudentAttendance/',views.AddStudentAttendance,name="AddStudentAttendance"),
    path('EbookViewf/',views.EbookViewf,name="EbookViewf"),
    path('viewattendencef/',views.viewattendencef,name="viewattendencef"),
    path('addEbookViewf/',views.addEbookViewf,name="addEbookViewf"),
    path('Assignmentviewadd/',views.Assignmentviewadd,name="Assignmentviewadd"),
    path('studentevents/',views.studentevents,name="studentevents"),
    

]
