# Generated by Django 2.0.5 on 2018-05-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180522_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rok', models.IntegerField(default=0)),
                ('przychody', models.IntegerField(default=0)),
                ('zysk_brutto', models.IntegerField(default=0)),
                ('dzialalnosc_operacyjna', models.IntegerField(default=0)),
                ('dzialalnosc_finansowa', models.IntegerField(default=0)),
                ('zysk_netto', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='DanePrzychody',
        ),
        migrations.DeleteModel(
            name='DaneRok',
        ),
    ]
