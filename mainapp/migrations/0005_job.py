# Generated by Django 4.0.4 on 2022-04-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_profile_email_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('ctc', models.IntegerField(default=0, null=True)),
                ('description', models.TextField()),
                ('mailto', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
