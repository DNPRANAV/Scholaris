# Generated by Django 2.0.6 on 2018-12-02 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_Designing', '0002_auto_20181201_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='date',
        ),
        migrations.AlterField(
            model_name='test',
            name='time',
            field=models.DateTimeField(),
        ),
    ]