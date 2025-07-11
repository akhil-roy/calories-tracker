from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal
from .forms import MealForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')
    meals = Meal.objects.filter(user = request.user).order_by('-date','-time')

    if from_date and to_date:
        meals = meals.filter(date__range=[from_date,to_date])
    
    total_calories = sum(m.calories for m in meals)
    expected = request.user.profile.expected_calories
    
    context = {
        "meals" : meals,
        "total_calories" : total_calories,
        "expected" : expected
    }

    return render(request, 'meals/dashboard.html', context)

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('dashboard')
    else:
        form = MealForm()
    return render(request,'meals/meals_form.html',{"form":form})

@login_required
def edit_meal(request, pk):
    meal = get_object_or_404(Meal,pk=pk,user=request.user)
    form = MealForm(request.POST or None,instance=meal)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request,'meals/meals_form.html',{"form":form})

@login_required
def delete_meal(request,pk):
    meal = get_object_or_404(Meal, pk=pk,user=request.user)
    meal.delete()
    return redirect('dashboard')
