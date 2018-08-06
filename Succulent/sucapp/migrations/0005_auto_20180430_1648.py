# Generated by Django 2.0.2 on 2018-04-30 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucapp', '0004_maintain_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hybridize',
            name='femaleParent',
        ),
        migrations.RemoveField(
            model_name='hybridize',
            name='maleParent',
        ),
        migrations.RemoveField(
            model_name='hybridize',
            name='progeny',
        ),
        migrations.RenameField(
            model_name='sucinfo',
            old_name='leafColor',
            new_name='leafcolor',
        ),
        migrations.RenameField(
            model_name='sucinfo',
            old_name='leafDent',
            new_name='leafopex_color',
        ),
        migrations.RenameField(
            model_name='sucinfo',
            old_name='leafShape',
            new_name='leafshape',
        ),
        migrations.RenameField(
            model_name='sucinfo',
            old_name='lightTime',
            new_name='lighttime',
        ),
        migrations.RenameField(
            model_name='sucinfo',
            old_name='plantShape',
            new_name='plantshape',
        ),
        migrations.DeleteModel(
            name='Hybridize',
        ),
    ]
