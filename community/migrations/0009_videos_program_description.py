# Generated by Django 5.1 on 2024-10-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_videos_program_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='program_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
