# Generated by Django 3.2.5 on 2021-07-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company_id', models.CharField(max_length=100)),
                ('NACCS_code', models.CharField(max_length=100)),
            ],
        ),
    ]
