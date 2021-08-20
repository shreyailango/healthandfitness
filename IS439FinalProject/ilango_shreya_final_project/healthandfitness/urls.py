from django.conf.urls import include, url
from django.urls import path
from .views import createUser, homepage, my_profile
from . import views


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),

    path("home/", homepage, name="homepage"),

    path("register/", createUser, name="register"),

    path("profile/", my_profile, name="my_profile"),

    path("posts/", views.show_post, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.new_post, name="new_post"),
    path("post/<int:pk>/edit", views.post_edit, name="post_edit"),
    path("post/<int:pk>/delete", views.post_delete, name="post_delete"),

    path("recipes/", views.show_recipe, name="recipe_list"),
    path("recipe/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/new/", views.new_recipe, name="new_recipe"),
    path("recipe/<int:pk>/edit", views.recipe_edit, name="recipe_edit"),
    path("recipe/<int:pk>/delete", views.recipe_delete, name="recipe_delete"),

    path("workouts/", views.show_workout, name="workout_list"),
    path("workout/<int:pk>/", views.workout_detail, name="workout_detail"),
    path("workout/new/", views.new_workout, name="new_workout"),
    path("workout/<int:pk>/edit", views.workout_edit, name="workout_edit"),
    path("workout/<int:pk>/delete", views.workout_delete, name="workout_delete")



]
