from django.contrib import admin
from django.urls import path
from customer import views



urlpatterns = [
  

    path('home', views.home,name="home"),
    path('signin',views.signup,name="signup"),
    path('login',views.alogin,name="login"),
    path('catering',views.catering),




            
          
            




            

          
           
       
   


]