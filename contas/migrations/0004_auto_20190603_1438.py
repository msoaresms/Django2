# Generated by Django 2.2.2 on 2019-06-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20190603_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
