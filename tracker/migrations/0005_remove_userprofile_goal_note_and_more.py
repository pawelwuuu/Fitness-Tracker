# Generated by Django 5.1.7 on 2025-06-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_userprofile_goal_note_userprofile_target_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='goal_note',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='target_weight',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]
