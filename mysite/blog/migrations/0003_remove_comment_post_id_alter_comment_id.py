# Generated by Django 4.1.2 on 2022-10-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="post_id",
        ),
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
