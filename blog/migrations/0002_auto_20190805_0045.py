# Generated by Django 2.2.3 on 2019-08-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='blog_post', to='organiser.Tag'),
        ),
    ]
