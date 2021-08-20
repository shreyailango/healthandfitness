from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Recipe, Workout


class NewUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        if commit:
            user.save()
        return user


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")

        # def __init(self, user, *args, **kwargs):
        #     self.user = user
        #     super(NewPost, self).__init__(*args, **kwargs)


class NewRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("title", "details", "photo")


class NewWorkout(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ("instructor", "title", "url", "details")