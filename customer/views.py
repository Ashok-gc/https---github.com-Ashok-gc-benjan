# import imp
import imp
from django.shortcuts import render, redirect
from customer.forms import CustomerForm, CateringForm, Updatecustomer
from customer.models import Customer, catering
from django.contrib.auth import authenticate, login


# Create your views here.


def signup(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        try:
            # print(form)
            result = form.save()
            request.session['customer_id'] = result.customer_id
            return redirect("/home")

        except:
            print("invalid")

    else:

        form = CustomerForm()
        print("invalid")

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def alogin(request):
    print(request)
    if request.method == 'POST':

        customer_name = request.POST.get("username")

        customer_pasword = request.POST.get("password")

        try:

            user = Customer.objects.get(
                username=customer_name, password=customer_pasword)

            if user is not None:

                request.session['username'] = user.username

                # request.session['email']=user.customer_email

                return redirect("/food1/form")

        except:

            admin = authenticate(request, username=customer_name,password=customer_pasword)

            if admin is not None:

                    login(request, admin)

                    # print(request.user.username)

                    return redirect ("home")
            return render("/signin")



    else:

        print("invalid")


    return render(request, 'login.html')



def Catering(request):
    if request.method == "POST":
        form = CateringForm(request.POST)
        # try:
        # print(form)
        form.save()
        return redirect("/customer/home")

        # except:
        #     print("invalid")

    else:

        form = CateringForm()
        print("invalid")

    return render(request, 'catering.html', {'form': form})

def cdisplay(request):
    customers = Customer.objects.all()
    return render(request, 'benjan admin/customers.html', {'customers': customers})

def cedit(request, p_id):

    customers = Customer.objects.get(customer_id=p_id)

    return render(request, "benjan admin/update_customer.html", {'customers': customers})
def update(request,p_id):

    #data verification

    customers=Customer.objects.get(customer_id=p_id)

    #bind data in form with instance of customer

    form =Updatecustomer(request.POST, instance=customers)

    if form.is_valid():

        try:

            form.save()

            return redirect("/customer")

        except:

            print("validation false")

    return render(request,"benjan admin/update_customer.html",{'customers':customers})

def delete(request, p_id):

    customerss = Customer.objects.get(customer_id=p_id)
    customerss.delete()
    return redirect("/customer")

def codisplay(request):
    orders=catering.objects.all()
    return render(request,"benjan admin/catering_orders.html" , {'orders':orders})

def deletecat(request,catering_id):
    data = catering.objects.get(catering_id=catering_id)
    data.delete()
    return redirect("/coorders/")

def updatecat(request,catering_id):

    #data verification

    data=catering.objects.get(catering_id=catering_id)

    #bind data in form with instance of customer
    if request.method=="POST":
        form =CateringForm(request.POST, instance=data)

        if form.is_valid():

            try:

                form.save()

                return redirect("/coorders/")

            except:

                print("validation false")

    return render(request,"benjan admin/update_cateringorder.html",{'catering':data})
# def cart(request):
#     try:
#         if request.user.is_authenticated:
#             cart_items = CartItem.objects.all().filter(user=request.user)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_items = CartItem.objects.all().filter(cart=cart, is_active=True)
#     except:
#         # print("except")
#         pass
#     context = {
#         "cart_items": cart_items,
#     }
#     return render(request,"food_cart.html", context)


# def cart(request, total=0.0, quantity=0, cart_items=None):
#     try:
#         if request.user.is_authenticated:
#             cart_items = CartItem.objects.all().filter(user=request.user)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_items = CartItem.objects.all().filter(cart=cart, is_active=True)
#     except:
#         # print("except")
#         pass

#     context = {
#         "cart_items": cart_items,
#     }

#     return render(request, 'store/cart.html', context) 