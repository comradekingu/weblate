# Generated by Django 2.2.9 on 2020-02-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("trans", "0057_shapings")]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="resolved",
            field=models.BooleanField(db_index=True, default=False),
        )
    ]
