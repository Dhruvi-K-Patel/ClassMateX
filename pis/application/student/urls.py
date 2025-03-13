from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="Studentmainpage"),
    path('StudentLogin/',views.StudentLogin,name="StudentLogin"),
    path('logout_views/',views.logout_views,name="logout_views"),
    path('Dashboard/',views.Dashboard,name="StundetDashboard"),
    path('StudentRegister/',views.StudentRegister,name="StudentRegister"),
    path('FacultiesList',views.FacultiesList,name="FacultiesList"),
    path('StudentAssignment/',views.StudentAssignment,name="StudentAssignment"),
    path('departmentsview/',views.departmentsview,name="departmentsviewstudent"),
    path('timetable/',views.timetable,name="timetablestudent"),
    path('LabView/',views.LabView,name="LabViewstudent"),
    path('viewattendence/',views.viewattendence,name='viewattendence'),
    path('EbookView/',views.EbookView,name="EbookView"),
    path('sdAssignmentview/',views.sdAssignmentview,name="sdAssignmentview"),
    path('sdAssignmentview/',views.sdAssignmentview,name="sdAssignmentview"),
    path('studenteventsf/',views.studenteventsf,name="studenteventsf"),
    path('NoticeBoardStudent/',views.NoticeBoardStudent,name="NoticeBoardStudent"),
]
