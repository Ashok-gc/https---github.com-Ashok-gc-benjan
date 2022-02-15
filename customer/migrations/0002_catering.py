# Generated by Django 4.0.2 on 2022-02-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='catering',
            fields=[
                ('catering_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('c_Name', models.CharField(max_length=100)),
                ('c_number', models.CharField(max_length=100)),
                ('c_types', models.CharField(max_length=100)),
                ('c_p_number', models.CharField(max_length=100)),
                ('c_date', models.FileField(upload_to='')),
                ('c_address', models.CharField(max_length=100)),
                ('c_details', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'catering',
            },
        ),
    ]