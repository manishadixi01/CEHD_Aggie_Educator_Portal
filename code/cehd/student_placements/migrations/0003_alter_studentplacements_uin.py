# Generated by Django 4.0.3 on 2022-04-03 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('student_placements', '0002_studentplacements_student_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentplacements',
            name='uin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='core.person', to_field='uin'),
        ),
    ]
