# Generated by Django 5.1.7 on 2025-03-13 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0005_matrimonyprofile_temple_weddinghall"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MatrimonyProfile",
        ),
        migrations.DeleteModel(
            name="WeddingHall",
        ),
    ]
