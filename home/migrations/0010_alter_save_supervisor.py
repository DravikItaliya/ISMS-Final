# Generated by Django 3.2.13 on 2022-05-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220511_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='supervisor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]