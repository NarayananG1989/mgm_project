# Generated by Django 3.0.3 on 2020-09-03 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20200903_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testresult',
            old_name='answer_given',
            new_name='user_answer',
        ),
    ]
