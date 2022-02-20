from unicodedata import name
from django.contrib import admin
from django.urls import path
from food1 import views



urlpatterns = [
  

    # path('home', views.home,name="home"),
    path('form',views.food1,name="Form"),
    path('display',views.display,name="display"),
    path('sweets_display',views.sweets_display,name="sweets_display"),
    path('namkeen_display',views.namkeen_display,name="namkeen_display"),
    path('bakery_display',views.bakery_display,name="bakery_display"),    
    path('edit/<int:p_id>',views.edit,name="edit"),
    path('delete/<int:p_id>',views.delete,name="delete"),
    path('display_admin',views.display_admin),
    path('update/<int:p_id>',views.update,name="update"),

   
    path('blog',views.Blog,name="blog"),
    path('bloghome',views.blog_home),
    path('search',views.search_food),

    path('cart', views.cart, name='cart'),  
    path('add-to-cart/<int:food1_id>/', views.add_cart, name="add-to-cart"),
    path('remove_item/<int:cart_item_id>/', views.remove_cart_item, name="remove_item"),
    path('purchaseitem/<int:product_id>/', views.purchaseitem, name="purchaseitem"),


    path('admin-view-booking/', views.admin_view_booking_view, name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view, name='delete-order'),
    

    





            
          
            


]