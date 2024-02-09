# Generated by Django 5.0.1 on 2024-02-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_like_like_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like_status',
        ),
        migrations.AddField(
            model_name='like',
            name='status',
            field=models.CharField(choices=[('like', 'like'), ('not like', 'not like')], default='not like', max_length=255),
        ),
    ]