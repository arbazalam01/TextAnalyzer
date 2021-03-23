# Generated by Django 3.1.7 on 2021-03-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textanalyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='message',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]