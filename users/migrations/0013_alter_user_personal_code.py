# Generated by Django 5.0.6 on 2024-05-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_personal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='personal_code',
            field=models.CharField(default='bAA37BCc', editable=False, max_length=8, unique=True),
        ),
    ]
