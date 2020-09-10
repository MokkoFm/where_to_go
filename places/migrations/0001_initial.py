# Generated by Django 3.1.1 on 2020-09-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.CharField(max_length=400)),
                ('description_long', models.TextField()),
                ('lng', models.DecimalField(decimal_places=2, max_digits=19)),
                ('lat', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
    ]
