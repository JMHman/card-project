# Generated by Django 5.0.6 on 2024-05-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_personal_code_alter_numbers_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='personal_code',
            field=models.CharField(default='EAf1DfB7', max_length=8, unique=True),
        ),
    ]
