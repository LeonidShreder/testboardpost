# Generated by Django 3.0.7 on 2020-06-14 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200614_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Post'),
        ),
    ]
