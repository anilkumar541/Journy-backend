# Generated by Django 5.0.1 on 2024-02-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0005_alter_customuser_is_active_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
