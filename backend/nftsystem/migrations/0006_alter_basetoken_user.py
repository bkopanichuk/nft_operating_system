# Generated by Django 3.2.3 on 2021-05-27 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nftsystem', '0005_basetoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basetoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
        ),
    ]
