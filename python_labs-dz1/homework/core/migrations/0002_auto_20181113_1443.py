# Generated by Django 2.1.3 on 2018-11-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('name',), 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AddField(
            model_name='service',
            name='photo',
            field=models.ImageField(default='static/images/not_found.jpg', upload_to='services/%Y', verbose_name='Картинка услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Слаг'),
        ),
    ]
