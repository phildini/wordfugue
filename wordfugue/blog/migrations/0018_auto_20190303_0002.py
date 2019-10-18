# Generated by Django 2.1.5 on 2019-03-03 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_blogpage_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordfugueHomePage',
            fields=[
                ('blogindexpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.BlogIndexPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.blogindexpage',),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='restrict_to_site',
            field=models.BooleanField(default=False, verbose_name='Restrict to original site'),
        ),
    ]