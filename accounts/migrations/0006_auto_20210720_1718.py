# Generated by Django 3.2.4 on 2021-07-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210630_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='descrition',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
