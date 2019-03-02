# Generated by Django 2.1.5 on 2019-02-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190228_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateTimeField(verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]