# Generated by Django 4.0.4 on 2022-04-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('schedule', models.DateTimeField()),
                ('description', models.TextField()),
                ('event_image', models.URLField(max_length=500)),
            ],
        ),
    ]
