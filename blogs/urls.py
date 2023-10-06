from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='home'),
    path('posts',views.all_posts,name='posts'),
    path('posts/<slug:slug>',views.single_post,name='post_detail'),
    path('k',views.karbaran_list),
    path('p/',views.product_list,name='Product_list'),
    path('p/<slug:slug>',views.product_details,name='Product_detail'),
]