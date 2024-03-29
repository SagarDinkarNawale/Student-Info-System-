# Generated by Django 2.2.5 on 2019-09-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='website',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='ABC', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default='ABC', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(default='ABC', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(default='ABC', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='ABC', max_length=30),
        ),
    ]
