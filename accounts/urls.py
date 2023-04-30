from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('reservation_delete/<int:pk>', views.ReservationDeleteView.as_view(), name='reservation_delete'),
    path('reservation_update/<int:pk>', views.ReservationUpdateView.as_view(), name='reservation_update'),
    path('login/', views.Login.as_view(), name = 'login'),
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('change/', views.UserChangeView.as_view(), name = 'modification'),
    path('restaurant/<int:pk>/favorite/delete/', views.FavoriteDeleteView.as_view(), name='favorite_delete'),

]
