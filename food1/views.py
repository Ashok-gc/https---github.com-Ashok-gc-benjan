import imp
from django.shortcuts import render, redirect
from customer.models import Customer

from food1.forms import FoodForm, UpdateForm
from food1.models import Food1, Cart, CartItem

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




