# Generated by Django 5.0.6 on 2024-05-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_personal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='personal_code',
            field=models.CharField(default='692b3193', editable=False, max_length=8, unique=True),
        ),
    ]