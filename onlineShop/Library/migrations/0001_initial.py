# Generated by Django 3.1.4 on 2020-12-19 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
            ],
            options={
                'verbose_name': 'نویسنده',
                'verbose_name_plural': 'نویسندگان',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'موضوع',
                'verbose_name_plural': 'موضوع ها',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان کتاب')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('price', models.IntegerField(default=0, verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, null=True, upload_to='books/', verbose_name='تصویر')),
                ('vote', models.IntegerField(default=0)),
                ('is_exist', models.BooleanField(default=True, verbose_name='موجود')),
                ('select', models.CharField(default='book', max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.author', verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.category', verbose_name='موضوع')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب ها',
                'ordering': ['-vote'],
            },
        ),
    ]
