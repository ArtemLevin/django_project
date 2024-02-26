from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=0, max_value=100)
    status = forms.CharField(max_length=100)
    avatar = forms.ImageField(required=False)

class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    ingredients = forms.CharField(max_length=1000)
    cooking_process = forms.CharField(max_length=1000)
    cooking_time = forms.IntegerField(min_value=0, max_value=100)
    amount_of_servings = forms.IntegerField(min_value=0, max_value=100)
    calories = forms.IntegerField(min_value=0, max_value=1000)
    image = forms.ImageField(required=False)

class UploadImageForm(forms.Form):
    image = forms.ImageField(required=False)