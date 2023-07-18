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
    #WORK STATION
    path('workstation/', views.workstation, name='workstation'),
    path('add_workstation/', views.add_workstation, name='add_workstation'),
    path('workstation/<int:pk>/', views.workstation_detail, name='workstation_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
