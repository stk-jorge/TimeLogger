# Generated by Django 3.1.4 on 2020-12-13 04:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timeloggerApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name_text',
            new_name='emp_first_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
