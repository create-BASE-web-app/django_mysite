# Generated by Django 3.2.5 on 2022-02-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_snsimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='good',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
