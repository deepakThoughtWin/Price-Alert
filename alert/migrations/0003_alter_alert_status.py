# Generated by Django 4.0.6 on 2022-07-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0002_alert_status_alter_alert_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('deleted', 'deleted'), ('triggered', 'triggered')], max_length=20),
        ),
    ]
