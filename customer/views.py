# import imp
from django.shortcuts import render, redirect
from customer.forms import CustomerForm, CateringForm
from customer.models import Customer
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

                return redirect("/customer/home")

        except:

            admin = authenticate(request, username=customer_name,password=customer_pasword)

            if admin is not None:

                    login(request, admin)

                    # print(request.user.username)

                    return redirect ("/food1/form")
            return render("/customer/signin")



    else:

        print("invalid")


    return render(request, 'login.html')



def catering(request):
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
