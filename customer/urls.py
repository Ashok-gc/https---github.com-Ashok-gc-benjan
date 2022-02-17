from django.contrib import admin
from django.urls import path
from customer import views


urlpatterns = [

    path('home', views.home, name="home"),
    path('signin', views.signup, name="signup"),
    path('login', views.alogin, name="login"),
    path('catering', views.Catering),
    path('customer', views.cdisplay),
    path('update/<int:p_id>', views.update, name="update"),
    path('cedit/<int:p_id>', views.cedit, name="cedit"),
    path('delete/<int:p_id>', views.delete, name="delete"),
    path('coorders/', views.codisplay),
    path('', views.home, name="home"),
    path('deletecat/<slug:catering_id>', views.deletecat),
    path('updatecat/<slug:catering_id>',views.updatecat)
    # path('cart', views.cart, name='cart'),
]


