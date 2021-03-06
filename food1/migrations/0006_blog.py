# Generated by Django 4.0.2 on 2022-02-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food1', '0005_alter_cartitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('blog_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('blog_Name', models.CharField(blank=True, max_length=100)),
                ('blog_Photo', models.FileField(blank=True, upload_to='blog_images')),
                ('blog_description', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
