# Generated by Django 2.2 on 2019-04-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('source_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostalCodeMapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('postal_code', models.CharField(max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('short_name', models.CharField(blank=True, max_length=5, null=True)),
                ('timezone', models.CharField(blank=True, max_length=100, null=True)),
                ('source_id', models.CharField(blank=True, max_length=10, null=True)),
                ('cities', models.ManyToManyField(blank=True, related_name='included_cities', to='core.City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='country_name')),
                ('short_name', models.CharField(blank=True, max_length=5, null=True)),
                ('source_id', models.CharField(blank=True, max_length=10, null=True)),
                ('states', models.ManyToManyField(blank=True, related_name='included_states', to='core.State')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
