from django.urls import path
from . import views

app_name = 'show_recommend_outcome'

urlpatterns = [
    path('', views.all_items_show),
    #path('new/product_code/<int:product_code>/', views.new_items_show),
    #path('old/product_code/<int:product_code>/', views.old_items_show),
    path('merged/product_code/<int:product_code>/', views.merged_items_show),
]
