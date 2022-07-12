from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='/'),
    path('student-view/<str:pk>/', views.studentview, name='studentview'),
    path('add-student', views.addstudent, name='addstudent'),
    path('update-student/<str:pk>', views.updatestudent, name='updatestudent'),
    path('delete-student/<str:pk>', views.deletestudent, name='deletestudent'),
]

