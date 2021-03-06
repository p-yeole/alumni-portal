# Generated by Django 4.0.4 on 2022-04-27 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=50)),
                ('registration_no', models.IntegerField(null=True, unique=True)),
                ('passing_year', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('branch', models.CharField(choices=[('COMPS', 'COMPUTER ENGINEERING'), ('IT', 'INFORMATION TECHNOLOGY ENGINEERING'), ('EXTC', 'ELECTRONICS AND TELECOMMUNICATION ENGINEERING'), ('ETRX', 'ELECTRONICS ENGINEERING'), ('AIDS', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE ENGINEERING')], max_length=5)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('company', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image_url', models.URLField(default='', max_length=500)),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
