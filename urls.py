
from django.urls import path
from Myapp import views

urlpatterns = [
    
    path('', views.login_user, name='login'),
    path('register/',views.register, name='register' ),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('allstudents/', views.allstudents, name='allstudents'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:id>/', views.edit, name= 'edit'),
    path('delete/<int:id>/', views.delete, name= 'delete'),
   
]
