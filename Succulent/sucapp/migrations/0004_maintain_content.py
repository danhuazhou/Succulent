# Generated by Django 2.0.2 on 2018-04-30 06:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sucapp', '0003_auto_20180427_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintain',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]
