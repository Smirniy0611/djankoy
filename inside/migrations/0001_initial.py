# Generated by Django 4.2.4 on 2023-09-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('price', models.FloatField()),
                ('publiched', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]
