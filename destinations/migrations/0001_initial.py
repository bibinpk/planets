# Generated by Django 3.1.2 on 2020-11-01 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Country name')),
                ('small_pic', models.ImageField(upload_to='c_pics', verbose_name='Thumpnail')),
                ('large_pic', models.ImageField(upload_to='c_pics', verbose_name='Picture')),
                ('description', models.CharField(max_length=30, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, unique=True, verbose_name='Destination name')),
                ('small_pic', models.ImageField(upload_to='d_pics', verbose_name='Thumpnail')),
                ('large_pic', models.ImageField(upload_to='d_pics', verbose_name='Picture')),
                ('s_desc', models.CharField(max_length=30, verbose_name='small Description')),
                ('l_desc', models.TextField(verbose_name='Large Description')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.countries')),
            ],
            options={
                'verbose_name': 'Destinations',
            },
        ),
        migrations.CreateModel(
            name='popular_places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.destinations')),
            ],
            options={
                'verbose_name': 'Popular places',
            },
        ),
        migrations.CreateModel(
            name='popular_countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cou_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.countries')),
            ],
            options={
                'verbose_name': 'Popular Countries',
            },
        ),
    ]
