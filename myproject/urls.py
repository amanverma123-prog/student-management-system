from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from students import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/students/')),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('signup/', views.signup, name='signup'),
]