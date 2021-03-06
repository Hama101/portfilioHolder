# Generated by Django 3.2.9 on 2021-12-05 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('about', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('body', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfilio.portfolio')),
            ],
        ),
    ]
