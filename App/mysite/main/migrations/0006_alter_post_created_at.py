# Generated by Django 4.0.3 on 2022-06-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
