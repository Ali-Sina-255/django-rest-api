# Generated by Django 5.0.3 on 2024-03-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('main_text', models.TextField()),
                ('published_time', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
