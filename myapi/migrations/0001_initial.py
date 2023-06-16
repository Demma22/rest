# Generated by Django 4.1.7 on 2023-04-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=50)),
                ('residence', models.CharField(max_length=50, null=True)),
                ('dob', models.DateField(max_length=150, null=True)),
            ],
        ),
    ]
