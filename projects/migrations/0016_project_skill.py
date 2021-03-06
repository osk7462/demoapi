# Generated by Django 3.2.4 on 2021-07-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileInfo', '0008_remove_skill_project'),
        ('projects', '0015_alter_projectimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.ManyToManyField(related_name='project_skills', to='profileInfo.Skill'),
        ),
    ]
