# Generated by Django 5.0.2 on 2024-02-26 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cook_process',
            new_name='cooking_process',
        ),
    ]
