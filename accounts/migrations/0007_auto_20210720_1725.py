# Generated by Django 3.2.4 on 2021-07-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210720_1718'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TesteModel',
        ),
        migrations.AddField(
            model_name='customer',
            name='cpf',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
