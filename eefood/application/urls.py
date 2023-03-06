from . import views
from django.urls import path
from application import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name ='top'),
    path('restaurant/<name>', views.ItemDetailView.as_view(), name='restaurant'),
    path('post/', views.PostRestaurantView.as_view(), name='post'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name ='review'),
    path('review/new/', views.CreateReviewView.as_view(), name ='review_new'),
    path('review/<int:pk>/edit/', views.ReviewEditView.as_view(), name='review_edit'),
    path('review/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)