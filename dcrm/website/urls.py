from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.employee, name='employee'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('employee/<int:pk>', views.employee_detail, name='employee'),
    path('delete_employee/<int:pk>', views.delete_employee, name='delete_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    #WORKSTATION
    path('workstation/', views.workstation, name='workstation'),
    path('add_workstation/', views.add_workstation, name='add_workstation'),
    path('workstation/<int:pk>/', views.workstation_detail, name='workstation_detail'),
    path('update_workstation/<int:pk>', views.update_workstation, name='update_workstation'),
    path('delete_workstation/<int:pk>', views.delete_workstation, name='delete_workstation'),
    #PROJECT
    path('project/', views.project, name='project'),
    path('add_project/', views.add_project, name='add_project'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('update_project/<int:pk>', views.update_project, name='update_project'),
    path('delete_project/<int:pk>', views.delete_project, name='delete_project'),
    #Holograms
    path('hologram/', views.hologram, name='hologram'),
    path('add_hologram/', views.add_hologram, name='add_hologram'),
    #TASK
    path('task/', views.task, name='task'),
    path('add_task/', views.add_task, name='add_task'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
