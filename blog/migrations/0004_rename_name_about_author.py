# Generated by Django 4.1.7 on 2023-03-10 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_about_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='name',
            new_name='author',
        ),
    ]
