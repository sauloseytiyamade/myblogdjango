# Generated by Django 4.0.6 on 2022-07-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.CharField(default=1, max_length=1500),
            preserve_default=False,
        ),
    ]