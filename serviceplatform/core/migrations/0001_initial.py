# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-11 05:57
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(default='', max_length=255)),
                ('gender', models.CharField(default='', max_length=255)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('tel', models.CharField(default='', max_length=255)),
                ('company_num', models.CharField(default='', max_length=255)),
                ('contract_people', models.CharField(default='', max_length=255)),
                ('contract_tel', models.CharField(default='', max_length=255)),
                ('bank_branch', models.CharField(default='', max_length=255)),
                ('bank_account', models.CharField(default='', max_length=255)),
                ('account_name', models.CharField(default='', max_length=255)),
                ('remark', models.TextField(default='', max_length=255)),
                ('logout', models.BooleanField(default=False)),
                ('create_user', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('create_organization', models.CharField(default='', max_length=255)),
                ('general_bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=255)),
                ('number', models.CharField(default='', max_length=255)),
                ('key', models.CharField(default='', max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('id_card', models.CharField(default='', max_length=255, unique=True)),
                ('gender', models.CharField(default='', max_length=255)),
                ('nation', models.CharField(default='', max_length=255)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('org', models.CharField(default='', max_length=255)),
                ('card_start_date', models.CharField(default='', max_length=255)),
                ('card_end_date', models.CharField(default='', max_length=255)),
                ('head_image', models.CharField(default='', max_length=255)),
                ('address', models.TextField(default='', max_length=255)),
                ('social_security_number', models.CharField(default='', max_length=255)),
                ('unemployment_number', models.CharField(default='', max_length=255)),
                ('graduation', models.CharField(default='', max_length=255)),
                ('tel', models.CharField(default='', max_length=255)),
                ('remark', models.TextField(default='', max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceType', models.CharField(default='', max_length=255)),
                ('add_time', models.CharField(default='', max_length=255)),
                ('add_date', models.CharField(default='', max_length=255)),
                ('finger_data', models.TextField(default='', max_length=255)),
                ('fp_score', models.FloatField(default=0)),
                ('fp_result', models.CharField(default='', max_length=255)),
                ('scene_image', models.TextField(default='', max_length=255)),
                ('face_score', models.FloatField(default=0)),
                ('face_result', models.CharField(default='', max_length=255)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Device')),
                ('person', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='policy_types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PolicyTypes'),
        ),
    ]
