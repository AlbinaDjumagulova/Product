# Generated by Django 4.2.5 on 2023-09-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
    ]
