# Generated by Django 2.1.3 on 2019-11-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('account_num', models.CharField(max_length=32)),
                ('u_password', models.CharField(max_length=32)),
                ('left_money', models.IntegerField()),
                ('bank_type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_time', models.DateTimeField()),
                ('log_account_num', models.CharField(max_length=32)),
                ('out_money', models.IntegerField()),
                ('in_money', models.IntegerField()),
                ('money_left', models.IntegerField()),
                ('vs_name', models.CharField(max_length=32)),
                ('vs_account', models.CharField(max_length=32)),
            ],
        ),
    ]
