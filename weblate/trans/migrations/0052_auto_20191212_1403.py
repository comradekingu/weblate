# Generated by Django 2.2.5 on 2019-12-12 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("trans", "0051_auto_20191210_1356")]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="unit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_set",
                to="trans.Unit",
            ),
        ),
        migrations.AddField(
            model_name="suggestion",
            name="unit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trans.Unit",
            ),
        ),
    ]
