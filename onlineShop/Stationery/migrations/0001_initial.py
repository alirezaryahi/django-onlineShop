# Generated by Django 3.1.4 on 2020-12-19 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Stationery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to='stationeries/', verbose_name='تصویر')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('vote', models.IntegerField(default=0)),
                ('is_exist', models.BooleanField(default=True, verbose_name='موجود')),
                ('select', models.CharField(default='stationery', max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stationery.group', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'نوشت افزار',
                'verbose_name_plural': 'نوشت افزار ها',
                'ordering': ['-vote'],
            },
        ),
    ]
