# Generated by Django 5.2.2 on 2025-06-07 16:34

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=300)),
                ('apartment', models.CharField(max_length=255)),
                ('town', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('zip_code', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.address')),
            ],
        ),
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('is_individual', models.BooleanField(default=True)),
                ('is_organization', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('occupation', models.CharField(max_length=100)),
                ('service', models.TextField(max_length=150)),
                ('reason_joined', models.TextField(max_length=150)),
                ('created_at', models.DateTimeField(blank=True, default='', null=True)),
                ('approved', models.BooleanField(default=0)),
                ('address', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresss', to='app.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donors', to=settings.AUTH_USER_MODEL)),
                ('Organization', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='app.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_contributed', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('occupation', models.CharField(max_length=100)),
                ('service', models.TextField(max_length=150)),
                ('reason_joined', models.TextField(max_length=150)),
                ('is_individual', models.BooleanField(default=True)),
                ('is_organization', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('approved', models.BooleanField(default=0)),
                ('address', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='app.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_contributed', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('occupation', models.CharField(max_length=100)),
                ('service', models.TextField(max_length=150)),
                ('reason_joined', models.TextField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('approved', models.BooleanField(default=0)),
                ('address', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
