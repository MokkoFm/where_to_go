# Generated by Django 3.1.1 on 2020-09-14 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20200915_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
    ]