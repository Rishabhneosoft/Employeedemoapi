# Generated by Django 4.0.6 on 2022-07-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('address', models.TextField(max_length=100)),
                ('state', models.CharField(choices=[('WFH', 'WFH'), ('WFO', 'WFO')], max_length=100)),
                ('gender', models.TextField(max_length=10)),
            ],
        ),
    ]