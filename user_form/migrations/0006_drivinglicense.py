# Generated by Django 4.1.4 on 2022-12-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_form', '0005_militarystatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrivingLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
