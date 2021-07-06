# Generated by Django 3.2.5 on 2021-07-01 12:22

from django.db import migrations, models
import rest_hooks.models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_hooks', '0002_swappable_hook_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='hook',
            name='headers',
            field=models.JSONField(default=rest_hooks.models.get_default_headers),
        ),
    ]