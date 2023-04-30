from . import views
from django.urls import path
from application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name ='top'),
    path('restaurant/<name>', views.ItemDetailView.as_view(), name='restaurant'),
    path('post/', views.PostRestaurantView.as_view(), name='post'),
    path('reservation/<name>', views.ReservationView.as_view(), name='reservation'),
    path('reservation_detail/', views.ReservationDetailView.as_view(), name='reservation_detail'),
    path('restaurant_review/<str:pk>/', views.RestaurantReviewView.as_view(), name='restaurant_review'),
    path('restaurant_detail/<str:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('review_edit/<int:pk>', views.ReviewEditView.as_view(), name='review_edit'),
    path('review_delete/<int:pk>', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('higher_review/', views.HigherReviewListView.as_view(), name='higher_review'),
    path('tools/', views.ToolsView.as_view(), name='tools'),
    path('restaurant/<str:name>/favorite/', views.FavoriteView.as_view(), name='favorite'),
    path('add_menu/<str:pk>/', views.RestaurantMenuView.as_view(), name='add_menu'),
    path('menu/edit/<int:pk>/', views.MenuItemEditView.as_view(), name='menu_edit'),
    path('menu/delete/<int:pk>/', views.MenuItemDeleteView.as_view(), name='menu_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)