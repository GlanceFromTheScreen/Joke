# Generated by Django 4.1.2 on 2022-12-11 11:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jokes', '0007_alter_addition_marked_by_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='marked_by_users',
            field=models.ManyToManyField(blank=True, related_name='marked', to=settings.AUTH_USER_MODEL),
        ),
    ]
