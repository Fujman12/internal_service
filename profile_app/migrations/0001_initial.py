# Generated by Django 2.0 on 2017-12-19 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise_model', '0002_auto_20171219_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Profile name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ProfileResourceRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255, verbose_name='Task name')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_profile_resource_rule', to='profile_app.Profile')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_resource_rule', to='enterprise_model.Resource')),
            ],
            options={
                'verbose_name': 'Profile Resource Rule',
                'verbose_name_plural': 'Profile Resource Rules',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Treatment name')),
                ('description', models.TextField(verbose_name='Description')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_profile', to='profile_app.Profile')),
            ],
            options={
                'verbose_name': 'Treatment',
                'verbose_name_plural': 'Treatments',
                'ordering': ('-id',),
            },
        ),
    ]