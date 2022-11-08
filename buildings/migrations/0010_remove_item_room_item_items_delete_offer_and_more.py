# Generated by Django 4.1.2 on 2022-11-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("buildings", "0009_offer_offergeo_delete_test_offer_geo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="room",
        ),
        migrations.AddField(
            model_name="item",
            name="items",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="items", to="buildings.room"
            ),
        ),
        migrations.DeleteModel(
            name="Offer",
        ),
        migrations.DeleteModel(
            name="OfferGeo",
        ),
    ]
