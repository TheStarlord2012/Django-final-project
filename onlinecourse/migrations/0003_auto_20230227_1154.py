# Generated by Django 3.1.3 on 2023-02-27 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230227_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='coice_text',
            new_name='choice_text',
        ),
    ]
