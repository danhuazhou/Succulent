# Generated by Django 2.0.2 on 2018-04-27 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sucapp', '0002_auto_20180422_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hybridize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Maintain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('editDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期')),
                ('author', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='sucinfo',
            name='image',
            field=models.ImageField(upload_to='sucapp/'),
        ),
        migrations.AlterField(
            model_name='sucinfo',
            name='lightTime',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='hybridize',
            name='femaleParent',
            field=models.ManyToManyField(related_name='female', to='sucapp.SucInfo'),
        ),
        migrations.AddField(
            model_name='hybridize',
            name='maleParent',
            field=models.ManyToManyField(related_name='male', to='sucapp.SucInfo'),
        ),
        migrations.AddField(
            model_name='hybridize',
            name='progeny',
            field=models.ManyToManyField(related_name='progeny', to='sucapp.SucInfo'),
        ),
    ]