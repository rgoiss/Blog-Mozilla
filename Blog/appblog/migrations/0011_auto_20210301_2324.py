# Generated by Django 3.1.7 on 2021-03-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0010_auto_20210227_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(help_text='Author_name', max_length=20),
        ),
    ]
