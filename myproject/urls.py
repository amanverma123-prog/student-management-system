from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from students import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student-api')

urlpatterns = [
    path('', RedirectView.as_view(url='/students/')),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('api/', include(router.urls)),
]