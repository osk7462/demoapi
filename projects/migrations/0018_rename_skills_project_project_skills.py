# Generated by Django 3.2.4 on 2021-07-11 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_rename_skill_project_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='skills',
            new_name='project_skills',
        ),
    ]
