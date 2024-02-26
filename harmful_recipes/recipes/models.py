from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    status = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=None, null=True)
    first_login = models.DateTimeField(default=None, null=True)
    avatar = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(default="", max_length=100)
    ingredients = models.TextField()
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null = True)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=None, null=True)
    cooking_time = models.IntegerField(null=True)
    cooking_process = models.TextField()
    amount_of_servings = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)
    calories = models.IntegerField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.ingredients

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    comment_date = models.DateTimeField(auto_now=True)
    comment_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.text

