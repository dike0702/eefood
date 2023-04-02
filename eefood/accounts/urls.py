from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/<username>', views.ProfileView.as_view(), name = 'profile'),
    path('login/', views.Login.as_view(), name = 'login'),
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('change/', views.UserChangeView.as_view(), name = 'modification')
]
