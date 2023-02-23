from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'top'),
    # path('review/', views.Review.as_view(), name = 'review'),
    # path('home/', views.HomeView.as_view(), name = 'home'),
    # path('login/', views.LoginView.as_view(), name = 'login'),
    # path('logout/', views.LogoutView.as_view(), name = 'logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)