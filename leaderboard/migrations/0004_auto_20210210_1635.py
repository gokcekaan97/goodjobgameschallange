# Generated by Django 3.1.6 on 2021-02-10 16:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0003_auto_20210210_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]