# Generated by Django 2.0.4 on 2018-06-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmanager', '0004_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='user',
            new_name='eduser',
        ),
        migrations.AlterField(
            model_name='education',
            name='anofim',
            field=models.PositiveIntegerField(),
        ),
    ]
