# Generated by Django 3.1.4 on 2021-07-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
    ]
