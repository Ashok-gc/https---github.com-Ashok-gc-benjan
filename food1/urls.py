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

    path('add-to-cart/<int:food1_id>/', views.add_cart, name="add-to-cart"),
    path('cart', views.cart, name='cart'),





            
          
            




            

          
           
       
   


]