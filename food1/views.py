import imp
import re
from django.shortcuts import render, redirect
from customer.models import Customer

from food1.forms import FoodForm, UpdateForm, BlogForm
from food1.models import Food1, Cart, CartItem, blog, Orders
from django.contrib import messages

# Create your views here.


def food1(request):

    print(request.FILES)

    if request.method == "POST":

        forms = FoodForm(request.POST, request.FILES)

        forms.save()

        return redirect("/food1/form")

    else:

        foods = FoodForm()

    return render(request, 'benjan admin/admin_home.html', {'foods': foods})

    


def display(request):
    foods = Food1.objects.filter(Type='Chowmein')
    momos = Food1.objects.filter(Type='Momo')
    foods = Food1.objects.filter(Type='Chowmein')
    momos = Food1.objects.filter(Type='Momo')
    dosa = Food1.objects.filter(Type='Dosa')
    burger = Food1.objects.filter(Type='Burger')
    pizza = Food1.objects.filter(Type='Pizza')
    tea = Food1.objects.filter(Type='Tea')
    chaat = Food1.objects.filter(Type='Chaat')
    sandwich = Food1.objects.filter(Type='Sandwich')
    s_snacks = Food1.objects.filter(Type='S.Snacks')
    print(request.user.username)
    return render(request, 'snacks.html', {'foods': foods, 'momos': momos,'dosa':dosa,'burger':burger,'pizza':pizza,'tea':tea,'chaat':chaat,'sandwich':sandwich,'s_snacks':s_snacks})
    
    # print(request.Customer.username)
def sweets_display(request):
    laddu = Food1.objects.filter(Type='Laddu')
    barfi = Food1.objects.filter(Type='Barfi')
    peda = Food1.objects.filter(Type='Peda')
    s_sweets = Food1.objects.filter(Type='S.Sweets')
    print(request.user.username)
    return render(request, 'sweets.html', {'laddu': laddu, 'barfi': barfi,'peda':peda,'s_sweets':s_sweets})

def namkeen_display(request):
    samosa = Food1.objects.filter(Type='Samosa')
    bhujiya = Food1.objects.filter(Type='Bhujiya')
    chips = Food1.objects.filter(Type='Chips')
    s_namkeen = Food1.objects.filter(Type='S.Namkeen')
    print(request.user.username)
    return render(request, 'namkeen.html', {'samosa': samosa, 'bhujiya': bhujiya,'chips':chips,'s_namkeen':s_namkeen})

def bakery_display(request):
    cakes = Food1.objects.filter(Type='Cakes')
    bread = Food1.objects.filter(Type='Bread')
    cookies = Food1.objects.filter(Type='Cookies')
    donuts = Food1.objects.filter(Type='Donuts')
    print(request.user.username)
    return render(request, 'bakery.html', {'cakes': cakes, 'bread': bread,'cookies':cookies,'donuts':donuts})

def edit(request, p_id):

    foods = Food1.objects.get(food1_id=p_id)

    return render(request, "benjan admin/update_food.html", {'foods': foods})


def delete(request, p_id):

    foodss = Food1.objects.get(food1_id=p_id)
    foodss.delete()
    return redirect("/food1/display_admin")


def display_admin(request):
    foods = Food1.objects.all()

    return render(request, 'benjan admin/foods.html', {'foods': foods})


def update(request, p_id):

    # data verification

    customers = Food1.objects.get(food1_id=p_id)

    # bind data in form with instance of customer

    form = UpdateForm(request.POST, instance=customers)

    if form.is_valid():

        try:

            form.save()

            return redirect("/food1/display_admin")

        except:

            print("validation false")

    return render(request, "benjan admin/update_food.html", {'customers': customers})


def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def cart(request):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.all().filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart, is_active=True)
    except:
        # print("except")
        pass
    context = {
        "cart_items": cart_items,
    }
    return render(request,"food_cart.html", context)

def add_cart(request, food1_id):
    current_user = request.user
    print(current_user)
    product = Food1.objects.get(food1_id=food1_id)

    if request.method == "POST":
        product = Food1.objects.get(food1_id=food1_id)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(
            product=product, cart=cart).exists()
        if is_cart_item_exists:
            
            # messages.success(request, "Item Already In Cart")
            return redirect('display')
            # print("In cart")
        else:
            cart_item = CartItem.objects.create(
                product=product,
                cart=cart,
                user=current_user,
            )
            cart_item.save()
            # messages.success(request, "Item Added In Cart")
        return redirect('cart')

def remove_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    # messages.success(request, "Item Sucessfully Removed")
    return redirect('cart')

def purchaseitem(request, product_id):
    if request.method == "POST":
        current_user = request.user
        product = Food1.objects.get(food1_id=product_id)

        order = Orders(user=current_user, product=product)
        order.save()

        cart_item_id  = request.POST['cart_item_id']
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()

        messages.success(request, "Item Ordered")
        return redirect('cart')
        # return redirect('payment')

def admin_view_booking_view(request):
    order = Orders.objects.all()
    data = {
        'order': order,
    }
    return render(request, 'benjan admin/view_order.html', data)

def delete_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')

# def about_us(request,pk):
#     order=Orders.objects.get(id=pk)
#     order.delete()
#     return redirect('admin-view-booking')

def Blog(request):

    print(request.FILES)

    if request.method == "POST":

        forms = BlogForm(request.POST, request.FILES)

        forms.save()

        return redirect("/food1/form")

    else:

        blogs = BlogForm()

    return render(request, 'benjan admin/add_blog.html', {'blogs': blogs})

    


def blog_display(request):
    blogs = blog.objects.all()
    return render(request, 'benjan admin/customers.html', {'blogs': blogs})


def blog_home(request):
    blogs = blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})









def search_food(request):

    if request.method=="POST":

        searched=request.POST['searched']

        venues = Food1.objects.filter(Name__icontains=searched)

        return render(request, "search.html",{'searched':searched,'venues':venues})

    else:

        return render(request, "nav.html",{})


def aboutus(request):
    return render(request,"about_us.html")