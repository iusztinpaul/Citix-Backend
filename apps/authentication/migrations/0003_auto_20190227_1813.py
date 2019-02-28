# Generated by Django 2.1.7 on 2019-02-27 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_useraddress_userrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrating',
            old_name='starRating',
            new_name='star_rating',
        ),
        migrations.AlterField(
            model_name='userrating',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='star_rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
