# Generated by Django 5.0.4 on 2024-04-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
