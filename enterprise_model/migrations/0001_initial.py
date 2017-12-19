# Generated by Django 2.0 on 2017-12-19 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Domain name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Domain',
                'verbose_name_plural': 'Domains',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_identifier', models.CharField(max_length=255, verbose_name='External identifier')),
                ('data', models.TextField(verbose_name='Data')),
            ],
            options={
                'verbose_name': 'Instance',
                'verbose_name_plural': 'Instances',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Resource name')),
                ('description', models.TextField(verbose_name='Description')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_domain', to='enterprise_model.Domain')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='instance',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_resource', to='enterprise_model.Resource'),
        ),
    ]
