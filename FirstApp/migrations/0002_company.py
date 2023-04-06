# Generated by Django 4.2 on 2023-04-06 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=43)),
                ('company_city', models.CharField(max_length=23)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstApp.client')),
            ],
        ),
    ]