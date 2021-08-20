from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from .models import Post, Recipe, Workout
from .forms import NewUser, NewPost, NewRecipe, NewWorkout
from django.http import HttpResponseRedirect
# Create your views here.


def homepage(request):
    return render(request, "base.html")


def createUser(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('homepage')
    else:
        form = NewUser()
    return render(request, "registration/account.html", {"form": form})


def show_post(request):
    posts = Post.objects.all()
    return render(request, "healthandfitness/post.html", {"posts": posts})


def new_post(request):
    if request.method == "POST":
        form = NewPost(request.POST, request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = NewPost()
    return render(request, "healthandfitness/new_post.html", {"form": form})


def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'healthandfitness/post_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = NewPost(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = NewPost(instance=post)
    return render(request, 'healthandfitness/new_post.html', {'form': form})


def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('homepage')
    return render(request, "healthandfitness/confirm_delete.html")


def show_recipe(request):
    recipes = Recipe.objects.all()
    return render(request, "healthandfitness/recipe.html", {"recipes": recipes})


def new_recipe(request):
    if request.method == "POST":
        form = NewRecipe(request.POST, request.FILES, request.user)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = NewRecipe()
    return render(request, "healthandfitness/new_recipe.html", {"form": form})


def recipe_detail(request,pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'healthandfitness/recipe_detail.html', {'recipe': recipe})


def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = NewRecipe(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = NewRecipe(instance=recipe)
    return render(request, 'healthandfitness/new_recipe.html', {'form': form})


def recipe_delete(request,pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('homepage')
    return render(request, "healthandfitness/confirm_delete.html")


def show_workout(request):
    workouts = Workout.objects.all()
    return render(request, "healthandfitness/workout.html", {"workouts": workouts})


def new_workout(request):
    if request.method == "POST":
        form = NewWorkout(request.POST, request.user)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = NewWorkout()
    return render(request, "healthandfitness/new_workout.html", {"form": form})


def workout_detail(request,pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'healthandfitness/workout_detail.html', {'workout': workout})


def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        form = NewWorkout(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.save()
            return redirect('workout_list')
    else:
        form = NewWorkout(instance=workout)
    return render(request, 'healthandfitness/new_workout.html', {'form': form})


def workout_delete(request,pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        workout.delete()
        return redirect('my_profile')
    return render(request, "healthandfitness/confirm_delete.html")


def my_profile(request):
    user = request.user
    workouts = Workout.objects.filter(user=user)
    recipes = Recipe.objects.filter(user=user)
    posts = Post.objects.filter(author=user)
    return render(request, "healthandfitness/myprofile.html", {'workouts': workouts, 'recipes': recipes, 'posts': posts})


