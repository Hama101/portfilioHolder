# Generated by Django 3.2.9 on 2021-12-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfilio', '0004_alter_portfolio_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='CIN',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
