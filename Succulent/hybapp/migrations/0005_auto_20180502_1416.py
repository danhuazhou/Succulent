# Generated by Django 2.0.2 on 2018-05-02 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucapp', '0006_auto_20180430_1710'),
        ('hybapp', '0004_auto_20180501_2033'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hybridize',
            unique_together={('maleparent', 'femaleparent')},
        ),
    ]
