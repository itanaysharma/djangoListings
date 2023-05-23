from django.urls import path
from .import views


app_name = 'listings'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Listings Page
    path('all_listings/', views.all_listings, name='all_listings'),
    path('new_listing/', views.new_listing, name='new_listing'),
    path('all_listings/<detail_id>/', views.detail, name='detail'),
    path('my_listings/',views.my_listings, name='my_listings')
]