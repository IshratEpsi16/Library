from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from . import views
app_name = 'library'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_login/admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_login/admin_dashboard/issue_book',views.issue_book,name='issue_book'),
    path('admin_login/admin_dashboard/issue_book/edit/<int:id>/', views.edit, name='edit'),
    path('admin_login/admin_dashboard/issue_book/delete/<int:id>/', views.delete_fun, name='delete'),
    path('admin_login_fun/',views.admin_login_fun, name='admin_login_fun'), 
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('student_signup/',views.student_signup_form, name='student_signup'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_login_fun',views.student_login_fun,name='student_login_fun'),
    path('student_login/student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('student_login/student_dashboard/my_profile/',views.my_profile,name='my_profile'),
    path('admin_info/',views.admin_all_info, name='admin_info'),
    path('student_info',views.student_info,name='student_info'),
    path('student_logout/',views.student_logout,name='student_logout'),

    
    
    
    
    
    
    
    
    
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT )