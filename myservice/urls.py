from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home
from accounts.views import login_view, register_view, logout_view
from services.views import create
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("faq", views.faq, name="faq"),
    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', register_view, name="register"),
    path('accounts/logout/', logout_view, name="logout"),
    path('services/create', create, name="create"),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
