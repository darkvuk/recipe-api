# Generated by Django 5.0.3 on 2024-04-12 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ingredient_recipe_ingrediets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingrediets',
            new_name='ingredients',
        ),
    ]