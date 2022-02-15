import imp
from django.shortcuts import render, redirect

from food1.forms import FoodForm
from food1.models import Food1

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

    return render(request, 'snacks.html', {'foods': foods, 'momos': momos})


def edit(request, p_id):

    foods = Food1.objects.get(food1_id=p_id)

    return render(request, "benjan admin/update_food.html", {'foods': foods})
def delete(request, p_id):

    foodss = Food1.objects.get(food1_id=p_id)
    foodss.delete()
    return render(request, "benjan admin/foods.html")


def display_admin(request):
    foods = Food1.objects.all()

    return render(request, 'benjan admin/foods.html', {'foods': foods})




