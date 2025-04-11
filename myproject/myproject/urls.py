from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import custom_login_redirect
from django.views.generic import TemplateView

urlpatterns = [
    path('auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('kindergarten/', views.kindergarten, name='kindergarten'),
    path('grades123/', views.grades123, name='grades123'),
    path('grades45/', views.grades45, name='grades45'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('abc-songs/', views.abc_songs, name='abc_songs'),
    path('math-songs/', views.math_songs, name='math_songs'),
    path('alphabet/', views.alphabet, name='alphabet'),
    path('colors/', views.colors, name='colors'),
    path('numbers/', views.numbers, name='numbers'),
    path('shapes/', views.shapes, name='shapes'),
    path('redirect/', custom_login_redirect, name='custom_redirect'),
    path('auth-error/', TemplateView.as_view(template_name='auth-error.html'), name='auth_error'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    
    if hasattr(settings, 'MEDIA_URL') and hasattr(settings, 'MEDIA_ROOT'):
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
