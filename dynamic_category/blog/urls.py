from django.urls import path, re_path
from . import views

# namespace
app_name = 'blog'

urlpatterns = [

    re_path(r'^category/$',
            views.CategoryListView.as_view(), name='category_list'),
    re_path(r'^category/(?P<slug>[-\w]+)/$',
            views.CategoryDetailView.as_view(), name='category_detail'),

]