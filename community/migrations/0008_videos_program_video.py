# Generated by Django 5.1 on 2024-10-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_videos_completprogram'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='program_video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
