# Generated by Django 5.0.2 on 2024-02-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
    ]