# Generated by Django 3.2.8 on 2022-03-10 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messsage',
            new_name='message',
        ),
    ]