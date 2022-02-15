from django.contrib import admin
from django.urls import path
from food1 import views



urlpatterns = [
  

    # path('home', views.home,name="home"),
    path('form',views.food1,name="Form"),
    path('display',views.display,name="display"),
    path('edit/<int:p_id>',views.edit,name="edit"),
    path('delete/<int:p_id>',views.delete,name="delete"),
    path('display_admin',views.display_admin),




            
          
            




            

          
           
       
   


]