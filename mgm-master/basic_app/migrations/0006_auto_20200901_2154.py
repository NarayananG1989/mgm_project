# Generated by Django 3.0.3 on 2020-09-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_frame_frame_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='answer',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
